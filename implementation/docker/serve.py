import torch
from safetensors.torch import load_file
from transformers import BertTokenizer, BertForSequenceClassification
import json

MODEL_PATH = "/opt/ml/model"

class SentimentAnalyzer:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
        state_dict = load_file(f"{MODEL_PATH}/model.safetensors")
        self.model = BertForSequenceClassification.from_pretrained(MODEL_PATH, state_dict=state_dict)
        self.model.eval()

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return predictions.tolist()

def model_fn(model_dir):
    return SentimentAnalyzer()

def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        return json.loads(request_body)["text"]
    raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_text, model):
    return model.predict(input_text)

def output_fn(prediction, response_content_type):
    return json.dumps({"predictions": prediction})
