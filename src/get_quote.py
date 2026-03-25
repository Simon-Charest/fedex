from requests import Response, post
from typing import Any


def get_quote(url: str, token: str, account_number: str) -> dict[str, Any]:
    data: dict[str, Any] = {
        "accountNumber": {
            "value": account_number
        },
        "requestedShipment": {
            "shipper": {
                "address": {
                    "postalCode": "65247",
                    "countryCode": "US"
                }
            },
            "recipient": {
                "address": {
                    "postalCode": "72348",
                    "countryCode": "US"
                }
            },
            "pickupType": "DROPOFF_AT_FEDEX_LOCATION",
            "rateRequestType": [
                "ACCOUNT",
                "LIST"
            ],
            "requestedPackageLineItems": [
                {
                    "weight": {
                        "units": "LB",
                        "value": "10"
                    }
                }
            ]
        }
    }
    headers: dict[str, str] = {
        "Authorization": f"Bearer {token}"
    }
    response: Response = post(url, data, headers=headers)
    quote: dict[str, Any] = {}

    if response.status_code == 200:
        quote = response.json()

    else:
        print(response.json())

    return quote
