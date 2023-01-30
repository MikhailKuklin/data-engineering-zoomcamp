from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


@task(retries=3)
def extract_from_gcs(color: str, year: int, month: int) -> Path:
    """Download trip data from GCS"""
    gcs_path = f"data/{color}_tripdata_{year}-{month:02}.parquet"
    gcs_block = GcsBucket.load("prefect-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"../data/")
    return Path(f"../data/{gcs_path}")

@task()
def write_bq(df: pd.DataFrame) -> None:
    """Write DataFrame to BiqQuery"""

    gcp_credentials_block = GcpCredentials.load("prefect-gcp-creds")

    df.to_gbq(
        destination_table="dezoomcamp_west6.rides",
        project_id="prime-framing-374716",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append",
    )

@flow()
def etl_gcs_to_bq(color, year, month, log_prints=True):
    """Main ETL flow to load data into Big Query"""

    path = extract_from_gcs(color, year, month)
    df = pd.read_parquet(path)
    rows_df = int(len(df))
    write_bq(df)
    return rows_df


@flow(log_prints=True)
def etl_parent_flow(color, year, month):
    rows_all = 0
    for m in month:
        rows_df = etl_gcs_to_bq(color, year, m)
        rows_all += rows_df
    print(f"Number of rows preprocessed: {rows_all}")

if __name__ == "__main__":
    etl_parent_flow("yellow", "2019", [2,3])
