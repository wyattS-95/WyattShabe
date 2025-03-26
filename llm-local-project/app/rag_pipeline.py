from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline

# Load fine-tuned model
llm = HuggingFacePipeline(model="models/fine_tuned_llm")

# Set up FAISS-based retrieval
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local("faiss_index", embeddings)

def query_llm(question):
    docs = vector_store.similarity_search(question, k=5)
    context = " ".join([doc.page_content for doc in docs])
    return llm.predict(f"Context: {context}\n\nQuestion: {question}")
