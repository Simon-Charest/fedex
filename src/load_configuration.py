from io import TextIOWrapper
from json import load
from typing import Any


def load_configuration(file: str) -> Any:
    stream: TextIOWrapper = open(file)
    data: Any = load(stream)
    stream.close()

    return data
