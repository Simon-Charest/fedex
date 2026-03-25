from requests import Response, post
from typing import Any


def get_token(url: str, api_key: str, secret_key: str) -> dict[str, Any]:
    data: dict[str, str] = {
        "grant_type": "client_credentials",
        "client_id": api_key,
        "client_secret": secret_key
    }
    response: Response = post(url, data)
    token: dict[str, Any] = {}

    if response.status_code == 200:
        token = response.json()

    return token
