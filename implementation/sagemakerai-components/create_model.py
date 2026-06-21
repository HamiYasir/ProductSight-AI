import boto3

# Create a session using the 'sentimental-analysis-user' profile
session = boto3.Session(profile_name='sentimental-analysis-user')

# Create a SageMaker client using the session
sagemaker = session.client('sagemaker')

# Now you can call the SageMaker API with this user
response = sagemaker.create_model(
    ModelName="bert-sentiment-model",
    PrimaryContainer={
        "Image": "763104351884.dkr.ecr.us-east-1.amazonaws.com/huggingface-pytorch-inference:1.10-transformers4.17-cpu-py38-ubuntu20.04",
        "ModelDataUrl": "s3://bert-sentiment-model/models/bert-sentiment/model.tar.gz"
    },
    ExecutionRoleArn="arn:aws:iam::273354629178:role/SageMaker-Execution-Role"
)

sagemaker.create_endpoint_config(
    EndpointConfigName="bert-sentiment-endpoint-config",
    ProductionVariants=[
        {
            "VariantName": "bertVariant",
            "ModelName": "bert-sentiment-model",
            "InstanceType": "ml.m5.large",
            "InitialInstanceCount": 1
        }
    ],
    DataCaptureConfig={
        "EnableCapture": True,
        "InitialSamplingPercentage": 100,
        "DestinationS3Uri": "s3://bert-sentiment-logging/sagemaker-logs/",
        "CaptureOptions": [{"CaptureMode": "Input"}, {"CaptureMode": "Output"}]
    }
)

sagemaker.create_endpoint(
    EndpointName="bert-sentiment-endpoint",
    EndpointConfigName="bert-sentiment-endpoint-config"
)

# sagemaker.create_monitoring_schedule(
#     MonitoringScheduleName="bert-sentiment-monitoring",
#     MonitoringScheduleConfig={
#         "ScheduleConfig": {
#             "ScheduleExpression": "cron(0 0 ? * 2 *)"  # Runs every Monday at midnight UTC
#         },
#         "MonitoringJobDefinition": {
#             "MonitoringAppSpecification": {
#                 "ImageUri": "763104351884.dkr.ecr.us-east-1.amazonaws.com/sagemaker-model-monitor-analyzer"
#             },
#             "BaselineConfig": {
#                 "ConstraintsResource": {
#                     "S3Uri": "s3://bert-sentimental-monitoring/baseline/constraints.json"
#                 }
#             },
#             "MonitoringInputs": [{
#                 "EndpointInput": {
#                     "EndpointName": "bert-sentiment-endpoint",
#                     "LocalPath": "/opt/ml/processing/input"
#                 }
#             }],
#             "MonitoringOutputConfig": {
#                 "MonitoringOutputs": [{
#                     "S3Output": {
#                         "S3Uri": "s3://bert-sentimental-monitoring/monitoring-output/",
#                         "LocalPath": "/opt/ml/processing/output"
#                     }
#                 }]
#             },
#             "MonitoringResources": {
#                 "ClusterConfig": {
#                     "InstanceCount": 1,
#                     "InstanceType": "ml.m5.large",
#                     "VolumeSizeInGB": 5
#                 }
#             },
#             "RoleArn": "arn:aws:iam::273354629178:role/SageMaker-Execution-Role"
#         }
#     }
# )
