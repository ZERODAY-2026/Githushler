
import os
import time
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Connect to the Snowflake sample database."""
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
        database="SNOWFLAKE_SAMPLE_DATA",
        schema="TPCH_SF1",
    )


def run_query(sql):
    """Run one read-only SELECT query and return data plus evidence."""
    statement = sql.strip()

    # Basic guardrails; this is not a complete SQL security boundary.
    if not statement.upper().startswith("SELECT "):
        raise ValueError("Only SELECT queries are allowed.")

    if ";" in statement.rstrip(";"):
        raise ValueError("Only one SQL statement is allowed.")

    conn = get_connection()
    start = time.perf_counter()

    try:
        with conn.cursor() as cur:
            cur.execute(statement)
            rows = cur.fetchall()
            columns = [col[0] for col in cur.description]
            query_id = cur.sfqid

        df = pd.DataFrame(rows, columns=columns)

        return {
            "data": df,
            "sql": statement,
            "row_count": len(df),
            "query_id": query_id,
            "execution_time_seconds": round(
                time.perf_counter() - start, 3
            ),
        }
    finally:
        conn.close()
