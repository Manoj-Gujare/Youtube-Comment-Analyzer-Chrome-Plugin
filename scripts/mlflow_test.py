import mlflow
import dagshub
import random

# Set the MLflow tracking URI
dagshub.init(repo_owner='Manoj-Gujare', repo_name='Youtube-Comment-Analyzer-Chrome-Plugin', mlflow=True)
mlflow.set_tracking_uri("https://dagshub.com/Manoj-Gujare/Youtube-Comment-Analyzer-Chrome-Plugin.mlflow")

# Start an MLflow run
with mlflow.start_run():
    # Log some random parameters
    mlflow.log_param("param1", random.randint(1, 100))
    mlflow.log_param("param2", random.random())

    # Log some random metrics
    mlflow.log_metric("metric1", random.random())
    mlflow.log_metric("metric2", random.uniform(0.5, 1.5))

    print("Logged random parameters and metrics.")
