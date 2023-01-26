# 1. docker image build -t  ikhailkuklin/prefect:dezoomcamp .
# 2. Login: docker login
# 3. Push image: docker image push mikhailkuklin/prefect:dezoomcamp
# 4. Prefect UI -> Blocks -> Docker container
# Check prefect profile: prefect profile ls
# Specify url: prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"

# run agent: prefect agent start -q default
# then another window deploy: prefect deployment run etl-parent-flow/docker-flow -p "months=[1,2]"

FROM prefecthq/prefect:2.7.7-python3.9

COPY docker-requirements.txt .

RUN pip install -r docker-requirements.txt --trusted-host pypi.python.org --no-cache-dir

COPY flows /opt/prefect/flows
RUN mkdir /opt/prefect/data/