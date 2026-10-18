import os
from pathlib import Path

import pandas as pd
import snowflake.connector
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def get_connection():
    """Connect to Snowflake using environment variables."""
    required = [
        "SNOWFLAKE_ACCOUNT",
        "SNOWFLAKE_USERNAME",
        "SNOWFLAKE_PASSWORD",
        "SNOWFLAKE_WAREHOUSE",
    ]

    missing = [key for key in required if not os.getenv(key)]
    if missing:
        raise ValueError(
            f"Missing environment variables: {', '.join(missing)}"
        )

    return snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USERNAME"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
        enable_server_session_keep_alive_auto_detection=True,
        database="SNOWFLAKE_SAMPLE_DATA",
        schema="TPCH_SF1",
    )


def run_query(sql):
    """Execute a basic SELECT query and return a DataFrame."""
    if not sql.strip().upper().startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed.")

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            columns = [col[0] for col in cur.description]

        return pd.DataFrame(rows, columns=columns)
    finally:
        conn.close()