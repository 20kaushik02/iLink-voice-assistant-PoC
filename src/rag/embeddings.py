from sentence_transformers import SentenceTransformer

miniLM_model = SentenceTransformer("all-MiniLM-L6-v2")


class EmbeddingWrapper:
    def __init__(self, model=miniLM_model):
        self.model = model

    def embed(self, texts):
        if isinstance(texts, str):
            texts = [texts]
            return self.model.encode(texts).flatten()
        
        return self.model.encode(texts)
