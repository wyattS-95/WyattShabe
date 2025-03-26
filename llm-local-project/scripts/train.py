import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset

# Load dataset
dataset = load_dataset("json", data_files="data/training_data.json")

# Load base model (Mistral-7B) without 4-bit quantization on macOS
MODEL_NAME = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",         # Use FP16 instead of bitsandbytes
    device_map="auto",          # Automatically maps to available device
)

# Prepare model for LoRA training
model = prepare_model_for_kbit_training(model)

# LoRA configuration
lora_config = LoraConfig(
    r=8,                         
    lora_alpha=32,               
    lora_dropout=0.1,            
    task_type="CAUSAL_LM"        
)

model = get_peft_model(model, lora_config)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./models",
    per_device_train_batch_size=2,   
    per_device_eval_batch_size=2,
    num_train_epochs=2,              
    save_steps=100,
    logging_dir="./logs",
    evaluation_strategy="no",  # Disable evaluation
    save_strategy="epoch",
    push_to_hub=False,
    report_to="none"
)


# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"]
)

# Start fine-tuning
trainer.train()

# Save fine-tuned model
model.save_pretrained("models/fine_tuned_llm")
tokenizer.save_pretrained("models/fine_tuned_llm")

print("✅ Fine-tuning complete. Model saved in 'models/fine_tuned_llm'.")
