from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

def model_fn(model_dir):
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    return model, tokenizer

def predict_fn(input_data, model):
    model, tokenizer = model
    inputs = tokenizer(input_data, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    return torch.nn.functional.softmax(outputs.logits, dim=-1).tolist()
