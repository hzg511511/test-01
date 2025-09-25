import os
import boto3
from prefect import task, flow
from dotenv import load_dotenv

load_dotenv()

@task(log_prints=True)
def test_task():
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name='nyc3',
                            endpoint_url=os.getenv("ENDPOINT"),
                            aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
                            aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"))


    response = client.list_buckets()

    print(response)


@flow(name="测试流程", log_prints=True)
def test_flow():
    test_task()
