"""Module with fuctions uses in many other modules."""


import json
import os


def write(message: str | tuple[str], output_path: str) -> None:
    """Write message in json file.

    Args:
        message: str | tuple[str] - strings to write.
        output_path: str - file to write message.
    """
    dirname = os.path.dirname(output_path)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(output_path, 'w') as output_file:
        json.dump(message, output_file)
