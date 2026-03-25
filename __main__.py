from argparse import ArgumentParser, Namespace
from sys import argv
from typing import Any

from src.get_quote import get_quote
from src.get_token import get_token
from src.load_configuration import load_configuration


def main() -> None:
    arguments: Namespace = parse_arguments()
    configuration: dict[str, Any] = load_configuration("config.json")

    if arguments.quote:
        token: dict[str, Any] = get_token(configuration[configuration["environment"]]["auth_url"], configuration[configuration["environment"]]["client_id"], configuration[configuration["environment"]]["client_secret"])
        quote: dict[str, Any] = get_quote(configuration[configuration["environment"]]["rate_url"], token["access_token"], configuration[configuration["environment"]]["account_number"], arguments.postal_code)

        for service in quote["output"]["rateReplyDetails"]:
            rate = service["ratedShipmentDetails"][0]
            print(f"{service['serviceName']}: {rate['totalNetCharge']} {rate['currency']}")

    if arguments.token:
        token: dict[str, Any] = get_token(configuration[configuration["environment"]]["auth_url"], configuration[configuration["environment"]]["client_id"], configuration[configuration["environment"]]["client_secret"])
        print(token)

    print("** DONE **")


def parse_arguments() -> Namespace:
    argument_parser: ArgumentParser = ArgumentParser()
    argument_parser.add_argument("-q", "--quote", help="Get quote")
    argument_parser.add_argument("-t", "--token", action="store_true", help="Get token")
    arguments: Namespace = argument_parser.parse_args()

    if len(argv) == 1:
        argument_parser.print_help()
        exit()

    return arguments


if __name__ == "__main__":
    main()
