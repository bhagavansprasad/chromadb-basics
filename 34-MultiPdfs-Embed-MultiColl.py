import logging
from chromadb_utils import get_or_create_vector_db
from chromadb_utils import pdf_store_embeddings_in_vectordb
from embeddings_utils import get_pdf_embeddings

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def _pdf_create_embeddings(pdf_path, vdb_name, coll_name):
    collection = get_or_create_vector_db(vdb_name, coll_name)

    page_embeddings = get_pdf_embeddings(pdf_path)

    pdf_store_embeddings_in_vectordb(collection, page_embeddings)
    logging.info(f"Processed {pdf_path} and stored embeddings in collection '{coll_name}'")

def main():
    pdf_files = [
        {"path": "user_data/cholas.pdf",   "vdb_name": "vectDB/pdf-vectorDB", "collection": "cholas-embeddings"},
        {"path": "user_data/ramayan.pdf",  "vdb_name": "vectDB/pdf-vectorDB",  "collection": "ramayan-embeddings"},
        {"path": "user_data/mahabharata.pdf", "vdb_name": "vectDB/pdf-vectorDB", "collection": "mahabharata-embeddings"},
    ]
    
    for pdf in pdf_files:
        pdf_path = pdf["path"]
        vdb_name = pdf["vdb_name"]
        coll_name = pdf["collection"]
        _pdf_create_embeddings(pdf_path, vdb_name, coll_name)

if __name__ == "__main__":
    main()
