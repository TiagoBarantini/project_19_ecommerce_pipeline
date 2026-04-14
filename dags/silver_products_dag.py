from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow/src')

from silver.silver_products import run

with DAG(
    dag_id='silver_products',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='process_silver_products',
        python_callable=run
    )
