"""Main module for hw2."""

import logging
import sys

from . import hw2


def process_data(input_path: str, output_path: str):
    """Forward to hw2.aggregate_users_stats(), but gracefully handle exceptions.

    See docs for hw2.aggregate_users_stats()


    Args:
        input_path: path to a json file containing user stats
        output_path: path to an output file. json aggregate stats will be written there.
    """
    try:
        hw2.aggregate_users_stats(input_path, output_path)
    except Exception as err:
        logging.error(msg=str(err))
        sys.exit(1)
