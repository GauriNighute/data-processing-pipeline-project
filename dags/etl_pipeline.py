from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.extract_api_data import extract_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('etl_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False)

extract_api = PythonOperator(
    task_id='extract_api',
    python_callable=extract_data,
    dag=dag
)

sqoop_import = BashOperator(
    task_id='sqoop_import',
    bash_command='sh /opt/airflow/scripts/sqoop_import.sh',
    dag=dag
)

spark_transform = BashOperator(
    task_id='spark_transform',
    bash_command='spark-submit --master yarn /opt/airflow/spark_jobs/transform_data.py',
    dag=dag
)

glue_load = BashOperator(
    task_id='glue_load',
    bash_command='python3 /opt/airflow/glue_jobs/load_to_snowflake.py',
    dag=dag
)

extract_api >> sqoop_import >> spark_transform >> glue_load
