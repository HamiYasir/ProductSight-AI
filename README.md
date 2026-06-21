# ProductSight AI - Intelligent Product Sentiment Analysis on AWS

A cloud-native sentiment analysis platform that leverages a BERT-based Natural Language Processing (NLP) model hosted on AWS to analyze product reviews in real time.

ProductSight AI demonstrates how Machine Learning, Serverless Computing, Monitoring, Logging, and Analytics services can be integrated into a complete AWS-based AI application. Users can submit product reviews through a web interface and receive sentiment predictions while administrators gain insights through monitoring and analytics dashboards.

## PROJECT GOAL

The objective of this project is to build an end-to-end sentiment analysis platform capable of processing product reviews and determining customer sentiment using a BERT-based transformer model.

The platform provides:

* Real-time sentiment prediction
* Serverless model inference
* Centralized monitoring and alerting
* Logging and analytics pipelines
* Cloud-native deployment using AWS services

The system is designed to demonstrate how Machine Learning models can be deployed and operated in a production-like AWS environment.

## THINGS THAT I LEARNED FROM THIS PROJECT

* Deploying Transformer-based NLP models on Amazon SageMaker
* Hosting Machine Learning models using AWS managed services
* Building serverless APIs using AWS Lambda and API Gateway
* Monitoring production ML endpoints using CloudWatch
* Configuring SNS-based alerting systems
* Logging model inference data using DynamoDB
* Building ETL pipelines using AWS Glue
* Creating analytics dashboards using Amazon QuickSight
* Hosting frontend applications using AWS Amplify
* Managing permissions using AWS IAM
* Designing cloud-native machine learning architectures
* Building scalable and maintainable AWS solutions

## AWS SERVICES AND TECHNOLOGIES USED

- Machine Learning

    - [BERT (Bidirectional Encoder Representations from Transformers)](https://huggingface.co/docs/transformers/index): The core NLP model used for sentiment classification of product reviews.

    - [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
    : Provides the pre-trained transformer architecture used for model deployment.

    - [PyTorch](https://pytorch.org/): Deep learning framework used for model training and inference.

    - [Amazon SageMaker](https://aws.amazon.com/sagemaker/): Hosts the trained BERT model and provides scalable inference endpoints that generate sentiment predictions.

- Serverless Inference Layer

    - [AWS Lambda](https://aws.amazon.com/lambda/): Executes serverless functions that invoke the SageMaker endpoint and process sentiment predictions and handles inference requests without requiring dedicated servers.

    - [Amazon API Gateway](https://aws.amazon.com/api-gateway/): Exposes REST APIs that allow the frontend application to communicate securely with the sentiment analysis backend.

- Storage and Logging

    - [Amazon DynamoDB](https://aws.amazon.com/dynamodb/): Stores inference logs including user input, prediction results, timestamps, and response metrics.

    - [Amazon S3](https://aws.amazon.com/s3/): Stores model artifacts, analytics datasets, and processed logging data.

    - [AWS Glue](https://aws.amazon.com/glue/): Transfers and transforms logged inference data from DynamoDB into S3 for analytics processing.

- Monitoring and Alerting

    - [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/): Monitors model performance, latency, invocation counts, and endpoint failures.

    - [Amazon SNS](https://aws.amazon.com/sns/): Sends email notifications whenever critical CloudWatch alarms are triggered.

- Monitored Metrics:

    - `Invocation5XXErrors`: Tracks server-side failures occurring within the SageMaker endpoint. Indicates issues such as model crashes, container failures, resource exhaustion, or endpoint misconfigurations. Monitoring this metric helps identify situations where the model is unable to process requests successfully.
    - `ModelLatency`: Measures the time taken by the deployed BERT model to generate a prediction. Helps evaluate the responsiveness of the inference endpoint. Sudden increases in latency may indicate resource bottlenecks, inefficient model execution, or unusually high workloads. Monitoring latency ensures a smooth user experience for real-time sentiment analysis.
    - `Invocations`: Records the total number of prediction requests received by the endpoint. Helps understand usage patterns and traffic trends. Can be used to detect unexpected traffic spikes that may impact endpoint performance. Assists in capacity planning and scaling decisions.

- Frontend

    - [AWS Amplify](https://aws.amazon.com/amplify/): Hosts the frontend application directly from a GitHub repository.

    - [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): Provides the structure of the user interface.

    - [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS): Styles the sentiment analysis dashboard.

    - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript): Sends user reviews to the backend and displays prediction results dynamically.

- Security and Access Management

    - [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/): Controls permissions and secure communication between AWS services.

- Analytics and Visualization

    - [Amazon QuickSight](https://aws.amazon.com/quicksight/): Generates dashboards and visualizations from collected sentiment data for business insights.

## SYSTEM ARCHITECTURE

### Architecture Diagram

![architecture_diagram](assets\architecture-diagram.png)

### Sentiment Analysis Pipeline

```text
User
 │
 ▼
AWS Amplify Frontend
 │
 ▼
Amazon API Gateway
 │
 ▼
AWS Lambda (bertSentimentLambda)
 │
 ▼
Amazon SageMaker Endpoint
 │
 ▼
BERT Sentiment Model
 │
 ▼
Prediction Response
 │
 ▼
Frontend
```

### Logging and Analytics Pipeline

```text
AWS Lambda (bertSentimentLogging)
 │
 ▼
Amazon DynamoDB
 │
 ▼
AWS Glue
 │
 ▼
Amazon S3
 │
 ▼
Amazon QuickSight
```

### Monitoring Pipeline

```text
Amazon SageMaker
 │
 ▼
Amazon CloudWatch
 │
 ▼
CloudWatch Alarms
 │
 ▼
Amazon SNS
 │
 ▼
Email Notifications
```

## MODEL ARTIFACTS

The trained BERT model artifacts have been hosted separately due to their large size.

[Download Model Files here](https://www.kaggle.com/models/hamiyasir/productsightai-models)

Included Artifacts:

- model.safetensors
- pytorch_model.bin
- BERT-model-to-host-in-s3
- bert-sentiment-model
- model-in-bucket-2

These files were originally packaged into a `model.tar.gz` archive and deployed to Amazon SageMaker through Amazon S3.

## AWS SERVICES USED

* AWS Amplify
* Amazon API Gateway
* AWS Lambda
* Amazon SageMaker
* Amazon S3
* Amazon DynamoDB
* AWS Glue
* Amazon CloudWatch
* Amazon SNS
* Amazon QuickSight
* AWS IAM

## PROJECT STATUS

This repository serves as a reconstruction and documentation of the original AWS implementation of ProductSight AI.

The project demonstrates the deployment of a BERT-based sentiment analysis system using a production-style AWS architecture incorporating inference, monitoring, logging, analytics, and serverless computing.

## DEPLOYMENT

This project has yet to be deployed :/