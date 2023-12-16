"""Process date."""

import json
import os
from datetime import date
from typing import Optional

import const
from user_statistics import AgeStatistics, DateStatistics


def process_data(input_path: str, output_path: str, current_date: Optional[date] = None) -> None:
    """Create or rewrite a json file with age and date statistics.

    Args:
        input_path: path to the input json file.
        output_path: path to the output json file.
        current_date: current date (used for tests).
    """
    try:
        with open(input_path, 'r') as input_file:
            studen_data = json.loads(input_file.read())
    except (FileNotFoundError, json.JSONDecodeError) as error:
        _write({'error-msg': error.strerror}, output_path)
        return

    statistics_by_name = {
        const.AGE_OUTPUT_FIELD_NAME: AgeStatistics(
            studen_data, const.AGE_INPUT_FIELD_NAME,
            const.OUTPUT_AGE_STATICTIC_FORM,
        ),
        const.DATE_OUTPUT_FIELD_NAME: DateStatistics(
            studen_data, const.DATE_INPUT_FIELD_NAME,
            const.OUTPUT_DATE_STATISTIC_FORM,
            current_date=current_date,
        ),
    }
    output = {}
    for name, statistics in statistics_by_name.items():
        output[name] = statistics.get_statistics()
    _write(output, output_path)


def _write(json_string: str, path):
    dirpath = os.path.dirname(path)
    if not os.path.exists(dirpath) and dirpath:
        os.makedirs(dirpath)
    with open(path, 'w') as output_file:
        json.dump(json_string, output_file)
