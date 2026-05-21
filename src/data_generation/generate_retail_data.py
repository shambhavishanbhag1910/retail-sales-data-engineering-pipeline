import os
import random
from datetime import datetime

import pandas as pd
from faker import Faker


fake = Faker()

RAW_DATA_PATH = "data/raw"


def ensure_raw_folder_exists():
    os.makedirs(RAW_DATA_PATH, exist_ok=True)


def generate_customers(num_customers=500):
    customers = []

    for customer_id in range(1, num_customers + 1):
        customers.append({
            "customer_id": customer_id,
            "customer_name": fake.name(),
            "email": fake.email(),
            "city": fake.city(),
            "state": fake.state(),
            "created_at": fake.date_between(start_date="-2y", end_date="today")
        })

    return pd.DataFrame(customers)


def generate_products(num_products=100):
    categories = [
        "Electronics",
        "Clothing",
        "Home",
        "Grocery",
        "Beauty",
        "Sports",
        "Books"
    ]

    products = []

    for product_id in range(1, num_products + 1):
        products.append({
            "product_id": product_id,
            "product_name": fake.word().title() + " " + fake.word().title(),
            "category": random.choice(categories),
            "unit_price": round(random.uniform(5, 500), 2),
            "supplier_id": random.randint(1, 20)
        })

    return pd.DataFrame(products)


def generate_orders(num_orders=1000, num_customers=500):
    order_statuses = ["completed", "cancelled", "returned", "pending"]
    payment_methods = ["credit_card", "debit_card", "upi", "cash", "net_banking"]

    orders = []

    for order_id in range(1, num_orders + 1):
        orders.append({
            "order_id": order_id,
            "customer_id": random.randint(1, num_customers),
            "order_date": fake.date_between(start_date="-1y", end_date="today"),
            "order_status": random.choices(
                order_statuses,
                weights=[75, 8, 7, 10],
                k=1
            )[0],
            "payment_method": random.choice(payment_methods)
        })

    return pd.DataFrame(orders)


def generate_order_items(num_orders=1000, num_products=100):
    order_items = []
    order_item_id = 1

    for order_id in range(1, num_orders + 1):
        number_of_items = random.randint(1, 5)

        for _ in range(number_of_items):
            quantity = random.randint(1, 5)
            unit_price = round(random.uniform(5, 500), 2)
            discount = round(random.uniform(0, 30), 2)

            order_items.append({
                "order_item_id": order_item_id,
                "order_id": order_id,
                "product_id": random.randint(1, num_products),
                "quantity": quantity,
                "unit_price": unit_price,
                "discount": discount
            })

            order_item_id += 1

    return pd.DataFrame(order_items)


def generate_inventory(num_products=100):
    inventory = []

    for product_id in range(1, num_products + 1):
        inventory.append({
            "product_id": product_id,
            "stock_quantity": random.randint(0, 500),
            "reorder_level": random.randint(20, 80),
            "last_updated": datetime.now().date()
        })

    return pd.DataFrame(inventory)


def save_dataframe(df, file_name):
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    df.to_csv(file_path, index=False)
    print(f"Generated file: {file_path} | Rows: {len(df)}")


def main():
    ensure_raw_folder_exists()

    num_customers = 500
    num_products = 100
    num_orders = 1000

    customers_df = generate_customers(num_customers)
    products_df = generate_products(num_products)
    orders_df = generate_orders(num_orders, num_customers)
    order_items_df = generate_order_items(num_orders, num_products)
    inventory_df = generate_inventory(num_products)

    save_dataframe(customers_df, "customers.csv")
    save_dataframe(products_df, "products.csv")
    save_dataframe(orders_df, "orders.csv")
    save_dataframe(order_items_df, "order_items.csv")
    save_dataframe(inventory_df, "inventory.csv")

    print("Retail source data generated successfully.")


if __name__ == "__main__":
    main()