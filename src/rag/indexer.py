from pathlib import Path
import glob
from doc_loader import PDFParser
from store import RetrievalWrapper

data_source_dir = Path(__file__).parent / ".." / ".." / "data" / "docs"

pdf_parser = PDFParser()
retriever = RetrievalWrapper()

# PDF docs
for doc_fullpath in data_source_dir.rglob("*.pdf"):
    doc_relpath = str(doc_fullpath.resolve().as_posix()).replace(
        str(data_source_dir.resolve().as_posix()), ""
    )
    doc_contents = pdf_parser.parse_and_clean(doc_fullpath.resolve())
    retriever.index_documents([doc_contents], [{"relpath": doc_relpath}])
