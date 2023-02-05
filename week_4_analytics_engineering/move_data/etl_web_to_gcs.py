from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from random import randint
from prefect.tasks import task_input_hash
from datetime import timedelta


#@task()
def fetch(dataset_url: str) -> pd.DataFrame:
    """Read FHV data from web into pandas DataFrame"""
    #df = pd.read_csv(dataset_url, encoding='latin1')
    df = pd.read_csv(dataset_url, low_memory=False)
    return df

#@task(log_prints=True)
def clean(df=pd.DataFrame) -> pd.DataFrame:
    """Fix dtype issues"""
    df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])
    df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])
    print(f"columns: {df.dtypes}")
    print(f"rows: {len(df)}")
    return df

#@task()
def write_local(df: pd.DataFrame, dataset_file: str) -> Path:
    """Write DataFrame out locally as parquet file"""
    path = Path(f"data/green/{dataset_file}.parquet")
    df.to_parquet(path, compression="gzip")
    return path

#@task()
def write_gcs(path: Path) -> None:
    """Upload local parquet file to GCS"""
    gcs_block = GcsBucket.load("prefect-gcs")
    gcs_block.upload_from_path(from_path=path, to_path=path)
    return

#@flow()
def etl_web_to_gcs(year: int, month: int) -> None:
    """The main ETL function"""
    dataset_file = f"green_tripdata_{year}-{month:02}"
    dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/{dataset_file}.csv.gz"

    df = fetch(dataset_url)
    df_clean = clean(df)
    path = write_local(df_clean, dataset_file)
    write_gcs(path)

#@flow()
def etl_parent_flow(
    months: list[int] = [1,2,3,4,5,6,7,8,9,10,11,12], years: list[int] = [2019,2020]
):
    for year in years:
        for month in months:
            etl_web_to_gcs(year, month)

if __name__ == "__main__":
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    years = [2019,2020]
    etl_parent_flow(months, years)
