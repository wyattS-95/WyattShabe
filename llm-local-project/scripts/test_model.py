import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load fine-tuned model
MODEL_PATH = "models/fine_tuned_llm"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto")

# Define test prompt
prompt = "What are the key points of the latest cybersecurity policy?"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

# Generate response
output = model.generate(**inputs, max_length=150)
print("Generated Response:\n", tokenizer.decode(output[0], skip_special_tokens=True))