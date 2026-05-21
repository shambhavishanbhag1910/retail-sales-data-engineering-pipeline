import os
import sys

import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.utils.db_connection import get_postgres_engine


RAW_DATA_PATH = "data/raw"


CSV_TABLE_MAPPING = {
    "customers.csv": "raw_customers",
    "products.csv": "raw_products",
    "orders.csv": "raw_orders",
    "order_items.csv": "raw_order_items",
    "inventory.csv": "raw_inventory",
}


def read_csv_file(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    return pd.read_csv(file_path)


def load_dataframe_to_postgres(df: pd.DataFrame, table_name: str):
    engine = get_postgres_engine()

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} records into table: {table_name}")


def ingest_all_files():
    for csv_file, table_name in CSV_TABLE_MAPPING.items():
        file_path = os.path.join(RAW_DATA_PATH, csv_file)

        print(f"Reading file: {file_path}")
        df = read_csv_file(file_path)

        print(f"Loading data into PostgreSQL table: {table_name}")
        load_dataframe_to_postgres(df, table_name)


def main():
    ingest_all_files()
    print("CSV ingestion completed successfully.")


if __name__ == "__main__":
    main()