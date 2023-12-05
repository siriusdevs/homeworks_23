"""Process date."""

import json

import const
from user_statistics import AgeStatistics, DateStatistics


def process_data(input_path: str, output_path: str) -> None:
    """Create or rewrite a json file with age and date statistics.

    Args:
        input_path (str): path to the input json file.
        output_path (str): path to the output json file.
    """
    with open(input_path, 'r') as input_file:
        studen_data = json.loads(input_file.read())
    statistics_by_name = {
        const.AGE_OUTPUT_FIELD_NAME: AgeStatistics(
            studen_data, const.AGE_INPUT_FIELD_NAME,
            const.OUTPUT_AGE_STATICTIC_FORM,
        ),
        const.DATE_OUTPUT_FIELD_NAME: DateStatistics(
            studen_data, const.DATE_INPUT_FIELD_NAME,
            const.OUTPUT_DATE_STATISTIC_FORM,
        ),
    }
    output = {}
    for name, statistics in statistics_by_name.items():
        output[name] = statistics.get_statistics()
    with open(output_path, 'w') as output_file:
        json.dump(output, output_file)
