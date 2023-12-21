"""Main module that provides statistics of JSON."""
from typing import Optional

import json_parsing as jp


def process_data(
    input_name: Optional[str] = 'data_hw2.json',
    output_name: Optional[str] = 'output.json',
) -> None:
    """Receives input JSON, creates output JSON containing email and registration years statistics.

    Args:
        input_name (str, optional): name of input JSON file to process.
            Defaults to 'data_hw2.json'.
        output_name (str, optional): name of output JSON file with statistics.
            Defaults to 'output.json'.
    """
    try:
        jp.assemble_data(input_name, output_name)
    except Exception as error:
        err_type = error.__class__.__name__
        jp.log_error_to_json(
            {'error': err_type, 'message': str(error)},
            output_name,
        )
