sagemaker.create_monitoring_schedule(
    MonitoringScheduleName="bert-sentiment-monitoring",
    MonitoringScheduleConfig={
        "ScheduleConfig": {
            # "ScheduleExpression": "cron(0 * * * ? *)"  # Runs every hour
            "ScheduleExpression": "cron(0 0 ? * 2 *)"  # Runs every Monday at midnight UTC
        },
        "MonitoringJobDefinition": {
            "BaselineConfig": {
                "ConstraintsResource": {
                    "S3Uri": "s3://bert-sentimental-monitoring/baseline/constraints.json"
                }
            },
            "MonitoringInputs": [{
                "EndpointInput": {
                    "EndpointName": "bert-sentiment-endpoint",
                    "LocalPath": "/opt/ml/processing/input"
                }
            }],
            "MonitoringOutputConfig": {
                "MonitoringOutputs": [{
                    "S3Output": {
                        "S3Uri": "s3://bert-sentimental-monitoring/monitoring-output/",
                        "LocalPath": "/opt/ml/processing/output"
                    }
                }]
            },
            "MonitoringResources": {
                "ClusterConfig": {
                    "InstanceCount": 1,
                    "InstanceType": "ml.m5.large",
                    "VolumeSizeInGB": 5
                }
            },
            "RoleArn": "arn:aws:iam::273354629178:role/SageMaker-Execution-Role"
        }
    }
)
