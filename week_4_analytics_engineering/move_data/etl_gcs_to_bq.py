from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


@task(retries=3)
def extract_from_gcs(color: str, year: int, month: int) -> Path:
    """Download trip data from GCS"""
    gcs_path = f"data/{color}/{color}_tripdata_{year}-{month:02}.parquet"
    gcs_block = GcsBucket.load("prefect-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"../data/{color}")
    return Path(f"../data/{color}/{gcs_path}")

@task()
def transform(path: Path) -> pd.DataFrame:
    """Data cleaning example"""
    df = pd.read_parquet(path)
    print(f"pre: missing passenger count: {df['passenger_count'].isna().sum()}")
    df["passenger_count"].fillna(0, inplace=True)
    print(f"post: missing passenger count: {df['passenger_count'].isna().sum()}")
    return df

@task()
def write_bq(color: str, df: pd.DataFrame) -> None:
    """Write DataFrame to BiqQuery"""

    gcp_credentials_block = GcpCredentials.load("prefect-gcp-creds")

    df.to_gbq(
        destination_table=f"trips_data_all.{color}_tripdata",
        project_id="prime-framing-374716",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append",
    )

@flow()
def etl_gcs_to_bq(color, year, month, log_prints=True):
    """Main ETL flow to load data into Big Query"""

    path = extract_from_gcs(color, year, month)
    df = transform(path)
    write_bq("green",df)

@flow(log_prints=True)
def etl_parent_flow(color,year, month):
    for m in month:
        rows_df = etl_gcs_to_bq(color, year, m)

if __name__ == "__main__":
    etl_parent_flow("green", "2020", [1,2,3,4,5,6,7,8,9,10,11,12])
