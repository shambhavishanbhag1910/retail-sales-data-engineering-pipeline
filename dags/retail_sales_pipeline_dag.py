from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


PROJECT_DIR = "/opt/airflow/retail-sales-data-engineering-pipeline"


default_args = {
    "owner": "data_engineering_team",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="retail_sales_data_engineering_pipeline",
    default_args=default_args,
    description="End to end retail sales data engineering pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["retail", "data-engineering", "etl", "elt", "dbt"],
) as dag:

    generate_retail_data = BashOperator(
        task_id="generate_retail_data",
        bash_command=f"cd {PROJECT_DIR} && python src/data_generation/generate_retail_data.py",
    )

    ingest_csv_to_postgres = BashOperator(
        task_id="ingest_csv_to_postgres",
        bash_command=f"cd {PROJECT_DIR} && python src/ingestion/ingest_csv_to_postgres.py",
    )

    run_python_data_quality_checks = BashOperator(
        task_id="run_python_data_quality_checks",
        bash_command=f"cd {PROJECT_DIR} && python src/validation/data_quality_checks.py",
    )

    run_dbt_transformations = BashOperator(
        task_id="run_dbt_transformations",
        bash_command=f"cd {PROJECT_DIR} && dbt run --project-dir dbt_project --profiles-dir profiles",
    )

    run_dbt_tests = BashOperator(
        task_id="run_dbt_tests",
        bash_command=f"cd {PROJECT_DIR} && dbt test --project-dir dbt_project --profiles-dir profiles",
    )

    (
        generate_retail_data
        >> ingest_csv_to_postgres
        >> run_python_data_quality_checks
        >> run_dbt_transformations
        >> run_dbt_tests
    )