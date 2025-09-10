import uuid
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

from rag.embeddings import EmbeddingWrapper


class RetrievalWrapper:
    def __init__(
        self,
        collection_name="documents",
        url="http://localhost:6333",
        vector_size=384,
    ):
        self.collection_name = collection_name
        self.vecdb_client = QdrantClient(url)
        self.distance_measure = Distance.COSINE
        if not self.vecdb_client.collection_exists(self.collection_name):
            self.vecdb_client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=vector_size, distance=self.distance_measure
                ),
            )
        self.embed_fn = EmbeddingWrapper().embed

    # simple window-based chunking
    def _chunk_document(self, doc, chunk_size=1000, overlap=100):
        chunks = []
        start = 0
        while start < len(doc):
            end = start + chunk_size
            chunk = doc[start:end]
            chunks.append(chunk)
            start = end - overlap  # slide window with overlap
            if start < 0:
                start = 0
        return chunks

    # ingestion
    def index_documents(self, documents, metadata=None):
        if metadata is None:
            metadata = [{} for _ in documents]

        # chunking
        chunks = []
        metas = []
        for doc, meta in zip(documents, metadata):
            for chunk in self._chunk_document(doc):
                chunks.append(chunk)
                metas.append(meta)  # duplicated for chunks of the same doc

        # generate embedding
        vectors = self.embed_fn(chunks)

        # indexing
        points = [
            PointStruct(
                id=str(uuid.uuid4()), vector=vec, payload={"text": chunk, **meta}
            )
            for chunk, vec, meta in zip(chunks, vectors, metas)
        ]

        self.vecdb_client.upsert(collection_name=self.collection_name, points=points)

    # retrieval
    def query(self, query_text, top_k=3):
        query_vector = self.embed_fn(query_text)

        results = self.vecdb_client.query_points(
            collection_name=self.collection_name, query=query_vector, limit=top_k
        )

        return [
            {
                "text": r.payload["text"],
                "score": r.score,
                "metadata": r.payload,
            }
            for r in results.points
        ]
