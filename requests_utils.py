import requests


async def get_http(url: str) -> dict:
    return requests.get(url).json()


def get_http_sync(url: str) -> dict:
    return requests.get(url).json()
