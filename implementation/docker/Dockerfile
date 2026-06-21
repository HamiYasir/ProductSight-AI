FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime

WORKDIR /opt/ml/code

RUN pip install transformers torch boto3 safetensors

COPY serve.py .

ENTRYPOINT ["python", "serve.py"]
