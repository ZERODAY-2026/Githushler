
from src.snowflake_client import run_query

sql = """
SELECT S_SUPPKEY, S_NAME
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER
ORDER BY S_SUPPKEY
LIMIT 5
"""

result = run_query(sql)

print("Rows retrieved:", result["row_count"])
print("Query ID:", result["query_id"])
print("Execution time:", result["execution_time_seconds"], "seconds")
print("\nExecuted SQL:\n", result["sql"])
print("\nResults:\n", result["data"].to_string(index=False))
