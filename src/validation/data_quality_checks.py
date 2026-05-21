import os
import sys

import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.utils.db_connection import get_postgres_engine


def read_table(table_name: str) -> pd.DataFrame:
    engine = get_postgres_engine()
    query = f"select * from {table_name}"
    return pd.read_sql(query, engine)


def check_not_null(df: pd.DataFrame, column_name: str, table_name: str):
    null_count = df[column_name].isnull().sum()

    if null_count > 0:
        raise ValueError(
            f"Data quality failed: {table_name}.{column_name} has {null_count} null values"
        )


def check_unique(df: pd.DataFrame, column_name: str, table_name: str):
    duplicate_count = df[column_name].duplicated().sum()

    if duplicate_count > 0:
        raise ValueError(
            f"Data quality failed: {table_name}.{column_name} has {duplicate_count} duplicate values"
        )


def check_positive_values(df: pd.DataFrame, column_name: str, table_name: str):
    invalid_count = (df[column_name] <= 0).sum()

    if invalid_count > 0:
        raise ValueError(
            f"Data quality failed: {table_name}.{column_name} has {invalid_count} non-positive values"
        )


def run_customer_checks():
    df = read_table("raw_customers")

    check_not_null(df, "customer_id", "raw_customers")
    check_unique(df, "customer_id", "raw_customers")
    check_not_null(df, "email", "raw_customers")

    print("raw_customers checks passed")


def run_product_checks():
    df = read_table("raw_products")

    check_not_null(df, "product_id", "raw_products")
    check_unique(df, "product_id", "raw_products")
    check_positive_values(df, "unit_price", "raw_products")

    print("raw_products checks passed")


def run_order_checks():
    df = read_table("raw_orders")

    check_not_null(df, "order_id", "raw_orders")
    check_unique(df, "order_id", "raw_orders")
    check_not_null(df, "customer_id", "raw_orders")

    print("raw_orders checks passed")


def run_order_item_checks():
    df = read_table("raw_order_items")

    check_not_null(df, "order_item_id", "raw_order_items")
    check_unique(df, "order_item_id", "raw_order_items")
    check_not_null(df, "order_id", "raw_order_items")
    check_not_null(df, "product_id", "raw_order_items")
    check_positive_values(df, "quantity", "raw_order_items")
    check_positive_values(df, "unit_price", "raw_order_items")

    print("raw_order_items checks passed")


def run_inventory_checks():
    df = read_table("raw_inventory")

    check_not_null(df, "product_id", "raw_inventory")
    check_unique(df, "product_id", "raw_inventory")

    print("raw_inventory checks passed")


def main():
    run_customer_checks()
    run_product_checks()
    run_order_checks()
    run_order_item_checks()
    run_inventory_checks()

    print("All data quality checks passed successfully.")


if __name__ == "__main__":
    main()