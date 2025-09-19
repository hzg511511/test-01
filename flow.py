from prefect import flow

@flow(log_prints=True)
def hello_world():
    print(f"Hello world from Prefect!")
