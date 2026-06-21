import boto3
import json

# Create a session using the 'sentimental-analysis-user' profile
session = boto3.Session(profile_name='sentimental-analysis-user')

# Create a SageMaker runtime client
runtime = session.client('sagemaker-runtime')

# Replace this with the text input you want to analyze
input_data = {
    "inputs": "Your input text here for sentiment analysis"
}

response = runtime.invoke_endpoint(
    EndpointName="bert-sentiment-endpoint",
    ContentType="application/json",
    Body=json.dumps(input_data)
)

result = json.loads(response['Body'].read().decode())
print(result)
