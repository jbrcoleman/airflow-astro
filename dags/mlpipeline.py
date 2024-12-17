from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

## Define tasks

def preprocess_data():
    print("Preprocessing data...")

def train_model():
    print("Training model")

def evaluate_model():
    print("Evaluate Models...")

# Define DAG

with DAG(
    'ml_pipeline',
    start_date=datetime(2024,1,1),
    schedule_interval='@weekly'
) as dag:

    preprocess = PythonOperator(task_id="preprocess_task",python_callable=preprocess_data)
    train=PythonOperator(task_id="train_task",python_callable=train_model)
    evaluate=PythonOperator(task_id="evaluate_task",python_callable=evaluate_model)

    # set dependencies
    preprocess >> train >> evaluate