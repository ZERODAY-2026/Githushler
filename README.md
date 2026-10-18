# PS1 — DataMind: Talk to Your Data

**Problem Statement:** Build an open-source data agent that lets users ask questions in natural language and receive answers grounded in real data, with traceable queries and evidence, transparent explanations, and honest handling of ambiguity, missing data, and unsupported requests.

# StockGuard — AI Supply-Chain Risk Investigator

StockGuard is our proposed solution for the DataMind problem statement. It aims to help users investigate supplier and order-related risks by asking questions in natural language and receiving evidence-backed findings from real Snowflake data.

## Planned Technology Stack

- **Snowflake:** Query and analyze real data at question time.
- **Google Gemma:** Interpret questions and help explain verified findings.
- **Python and Streamlit:** Build the application and user interface.

## Current Progress

- Verified access to Snowflake.
- Queried the Snowflake TPC-H sample supplier and part-supplier tables.
- Preparing the Gemma integration and application architecture.

## Data and Limitations

The initial prototype uses Snowflake's TPC-H sample data. Findings will be limited to what the available data supports; benchmark records will not be presented as proof of real-world supplier failures or actual stockouts.
