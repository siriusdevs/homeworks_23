"""Contain the implemented function from Vasilenko's second task."""
import json
import logging
from typing import NoReturn

from hw2.src.utils import UserStatsUtils, log_error_and_write_to_output_file

logging.basicConfig(
    level=logging.INFO,
)


def process_data(data_file_path: str, output_file_path: str) -> NoReturn:
    """Read users data from data_file \
        and write the necessary statistics by task into output_file.

    Args:
        data_file_path (str): the path to file with users data
        output_file_path (str): the path to file in which we save the necessary statistics
    """
    logger = logging.getLogger(__name__)
    user_stats_utils: UserStatsUtils = UserStatsUtils(data_file_path, output_file_path, logger)

    if not user_stats_utils.data_file_is_valid:
        log_error_and_write_to_output_file(
            error_msg=user_stats_utils.error_msg,
            output_file_path=output_file_path,
            logger=logger,
        )
        return

    with open(output_file_path, 'w') as output_file:
        json.dump(
            obj=user_stats_utils.user_stats,
            fp=output_file,
            indent=4,
            ensure_ascii=False,
        )
