# 1. docker image build -t  ikhailkuklin/prefect:dezoomcamp .
# 2. Login: docker login
# 3. Push image: docker image push mikhailkuklin/prefect:dezoomcamp
# 4. Prefect UI -> Blocks -> Docker container
# 5. Deploy flow: python flows/03_parameterization_deployment/docker_deploy.py 
# 6. Deployment build: prefect deployment build flows/03_parameterization_deployment/parameterized_flow.py:etl_parent_flow -n 'docker_flow4' -ib docker-container/dezoomcamp2
# 7.Check prefect profile: prefect profile ls
# Specify url: prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"
# 8. Start an agent: prefect agent start -q default
# 9. Run: prefect deployment run etl-parent-flow/docker-flow6 -p "months=[1,2]"

FROM prefecthq/prefect:2.7.7-python3.9

COPY docker-requirements.txt .

RUN pip install -r docker-requirements.txt --trusted-host pypi.python.org --no-cache-dir

COPY flows /opt/prefect/flows
COPY data /opt/prefect/data
#RUN mkdir /opt/prefect/data/yellow