import os
import json
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_PATH = "data/raw_data"
OUTPUT_PATH = "data/training_data.json"

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def process_documents():
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=100)
    dataset = []

    for file in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH, file)

        if file.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file.endswith(".txt"):
            text = extract_text_from_txt(file_path)
        else:
            continue  # Skip unsupported file types

        chunks = text_splitter.split_text(text)

        for chunk in chunks:
            dataset.append({"instruction": "Summarize this document", "input": chunk, "output": chunk[:100]})

    # Save dataset in JSON format
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=4)

    print(f"✅ Processed {len(dataset)} data points saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    process_documents()
