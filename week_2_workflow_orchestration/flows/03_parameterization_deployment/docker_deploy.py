from prefect.deployments import Deployment
from parameterized_flow import etl_parent_flow # copy our functions
from prefect.infrastructure.docker import DockerContainer

docker_block = DockerContainer.load("dezoomcamp2")

docker_dep = Deployment.build_from_flow(
    flow=etl_parent_flow,
    name="docker-flow3",
    infrastructure=docker_block,
)

if __name__ == "__main__":
    docker_dep.apply()
