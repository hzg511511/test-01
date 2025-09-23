from prefect import flow, task
import time

# 1. 定义任务：封装打印逻辑
@task(log_prints=True)  # 启用任务的日志打印
def print_hello():
    print(1+1)

# 2. 定义流程：调用任务
@flow(log_prints=True)
def hello_world():
    time.sleep(10)
    # 调用任务（Prefect会自动跟踪该任务的状态）
    print_hello()
