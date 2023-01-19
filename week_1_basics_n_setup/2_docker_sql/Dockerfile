FROM python:3.9.1

# install packages/libraries inside of container
RUN apt-get install wget 
RUN pip install pandas sqlalchemy psycopg2

# specify working directory and copy script there
WORKDIR /app
COPY ingest_data.py ingest_data.py 

# order of execution: python 3.9.1 will run ingest_data.py
ENTRYPOINT [ "python", "ingest_data.py" ]