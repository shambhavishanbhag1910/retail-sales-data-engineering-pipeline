import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine


BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

# Load .env values only if environment variables are not already supplied.
# This allows Docker/Airflow environment variables to override local .env.
load_dotenv(dotenv_path=ENV_PATH, override=False)


def get_postgres_engine():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    database = os.getenv("POSTGRES_DB")

    print(
        f"Connecting to PostgreSQL: user={user}, "
        f"host={host}, port={port}, database={database}"
    )

    connection_string = (
        f"postgresql://{user}:{password}@{host}:{port}/{database}"
    )

    engine = create_engine(connection_string)
    return engine