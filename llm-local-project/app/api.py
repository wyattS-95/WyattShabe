from fastapi import FastAPI
from rag_pipeline import query_llm

app = FastAPI()

@app.get("/query")
def query_model(question: str):
    response = query_llm(question)
    return {"answer": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
