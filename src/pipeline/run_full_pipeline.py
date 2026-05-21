import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]


def run_command(command: str, step_name: str):
    print("\n" + "=" * 80)
    print(f"Starting step: {step_name}")
    print("=" * 80)

    result = subprocess.run(
        command,
        shell=True,
        cwd=BASE_DIR,
        text=True
    )

    if result.returncode != 0:
        print(f"\nPipeline failed at step: {step_name}")
        sys.exit(result.returncode)

    print(f"\nCompleted step: {step_name}")


def main():
    print("\nRetail Sales Data Engineering Pipeline Started")

    run_command(
        "python src/data_generation/generate_retail_data.py",
        "Generate Retail Source Data"
    )

    run_command(
        "python src/ingestion/ingest_csv_to_postgres.py",
        "Ingest CSV Files into PostgreSQL Raw Tables"
    )

    run_command(
        "python src/validation/data_quality_checks.py",
        "Run Python Data Quality Checks"
    )

    run_command(
        "dbt run --project-dir dbt_project --profiles-dir profiles",
        "Run dbt Transformations"
    )

    run_command(
        "dbt test --project-dir dbt_project --profiles-dir profiles",
        "Run dbt Data Quality Tests"
    )

    print("\n" + "=" * 80)
    print("Retail Sales Data Engineering Pipeline Completed Successfully")
    print("=" * 80)


if __name__ == "__main__":
    main()