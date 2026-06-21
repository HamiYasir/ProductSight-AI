from safetensors.torch import load_file
import torch

# Load model weights from .safetensors
model_path = "model.safetensors"
model_weights = load_file(model_path)

# Save as Hugging Face-compatible .bin
torch.save(model_weights, "pytorch_model.bin")
print("Converted model.safetensors to pytorch_model.bin")
