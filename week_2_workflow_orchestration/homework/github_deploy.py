from prefect.deployments import Deployment
from etl_github_to_gcs import etl_web_to_gcs # copy our functions
from prefect.filesystems import GitHub

github_block = GitHub.load("zoomcamp")

github_dep = Deployment.build_from_flow(
    flow=etl_web_to_gcs,
    name="github-flow",
    infrastructure=github_block,
)

if __name__ == "__main__":
    github_dep.apply()