from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='customer_order_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    run_etl = BashOperator(
        task_id='run_etl',
        bash_command='python spark_jobs/transform.py'
    )

    validate = BashOperator(
        task_id='validate_data',
        bash_command='python spark_jobs/validate.py'
    )

    reporting = BashOperator(
        task_id='generate_report',
        bash_command='python spark_jobs/reporting.py'
    )

    run_etl >> validate >> reporting