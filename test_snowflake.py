from src.snowflake_client import run_query

sql = """
SELECT S_SUPPKEY, S_NAME
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER
ORDER BY S_SUPPKEY
LIMIT 5
"""

df = run_query(sql)

print("Retrieved rows:", len(df))
print(df.to_string(index=False))