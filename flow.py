import httpx
from prefect import flow

#@flow
def get_repo_info():
    #url = "https://api.github.com/repos/PrefectHQ/prefect"
    url = "https://github.com/PrefectHQ/prefect.git"
    response = httpx.get(url)
    #response.raise_for_status()
    #repo = response.json()
    print(f"PrefectHQ/prefect repository statistics:")


if __name__ == "__main__":
    get_repo_info()
