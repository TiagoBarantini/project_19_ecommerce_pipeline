from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow/src')

from bronze.bronze_carts import run

with DAG(
    dag_id='bronze_carts',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='extract_load_carts',
        python_callable=run
    )
