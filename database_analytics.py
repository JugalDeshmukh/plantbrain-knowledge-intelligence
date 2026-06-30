import os
import pandas as pd
import duckdb

def initialize_database_and_get_logs() -> pd.DataFrame:
    """
    Ensures target data directories exist, writes mock telemetry records 
    if absent, and loads logs into a pandas DataFrame.
    """
    if not os.path.exists("data"):
        os.makedirs("data")

    csv_path = "data/maintenance_logs.csv"
    if not os.path.exists(csv_path):
        mock_data = """log_id,timestamp,asset_id,asset_name,issue_description,status,downtime_hours
1,2026-06-15,PUMP-04,Primary Water Pump,Cavitation detected and seal leaking,RESOLVED,3.5
2,2026-06-20,VALVE-12,Main Gas Feed Valve,Slight pressure drop observed during shift change,OPEN,1.2
3,2026-06-22,COMP-01,Air Compressor,High vibration and thermal cutoff triggered,OPEN,4.0"""
        with open(csv_path, "w") as f:
            f.write(mock_data)

    return pd.read_csv(csv_path)

def run_downtime_metrics_query(df_logs: pd.DataFrame) -> pd.DataFrame:
    """
    Executes a rapid DuckDB SQL query to aggregate total downtime 
    and failure events grouped by asset.
    """
    query = """
        SELECT asset_name, SUM(downtime_hours) as total_downtime, COUNT(*) as failure_count
        FROM df_logs
        GROUP BY asset_name
        ORDER BY total_downtime DESC
    """
    return duckdb.query(query).to_df()

def get_open_issues(df_logs: pd.DataFrame) -> pd.DataFrame:
    """
    Queries active open anomalies within the telemetry log dataframe 
    to feed into compliance auditing systems.
    """
    query = "SELECT * FROM df_logs WHERE status = 'OPEN'"
    return duckdb.query(query).to_df()