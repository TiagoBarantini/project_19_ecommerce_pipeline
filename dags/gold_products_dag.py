from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow/src')

from gold.gold_products import run

with DAG(
    dag_id='gold_products',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='build_dim_produto',
        python_callable=run
    )
