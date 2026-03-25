from requests import Response, post
from typing import Any


def get_quote(url: str, token: str, account_number: str, postal_code: str) -> dict[str, Any]:
    json: dict[str, Any] = {
        "accountNumber": {
            "value": account_number
        },
        "requestedShipment": {
            "shipper": {
                "address": {
                    "postalCode": "J4G 1S8",
                    "countryCode": "CA"
                }
            },
            "recipient": {
                "address": {
                    "postalCode": postal_code,
                    "countryCode": "CA"
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
    response: Response = post(url, json=json, headers=headers)
    quote: dict[str, Any] = {}

    if response.status_code == 200:
        quote = response.json()

    else:
        print(response.json())

    return quote
