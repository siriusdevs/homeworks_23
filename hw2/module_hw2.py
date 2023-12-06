"""Auxiliary module for hw2."""
import json
import os


def median_age(data_age: list[int]) -> int:
    """Calculate the median age from a list of ages.

    Args:
    ----
        data_age (list): List of age values.

    Returns:
    -------
        int: Median age.
    """
    if data_age:
        data_age = sorted(data_age)
        len_data_age = len(data_age)
        if len_data_age % 2 == 1:
            return data_age[len_data_age // 2]
        age_index = len_data_age // 2
        return (data_age[age_index - 1] + data_age[age_index]) // 2
    return 0


def handle_error(message: str) -> None:
    """Handle errors by writing a JSON file with an error message.

    Args:
    ----
        message (str): Error message.
    """
    with open("error.json", "w") as error_file:
        json.dump({"error": message}, error_file)


def is_file_empty(input_path: str) -> bool:
    """Check if a file is empty.

    Args:
    ----
        input_path (str): Path of the file to check.

    Returns:
    -------
        bool: True if the file is empty, False otherwise.
    """
    if os.stat(input_path).st_size == 0:
        handle_error("Input file is empty.")
        return True
    return False


def check_path(input_path: str, output_path: str) -> bool:
    """Check the existence of the specified file path.

    Args:
    ----
        input_path (str): Path to the input file.
        output_path (str): Path to the input file.

    Returns:
    -------
        bool: True if the file does not exist, otherwise False.
    """
    if not os.path.exists(input_path):
        handle_error("Input file does not exist.")
        return True
    if not os.path.exists(output_path):
        handle_error("Output file does not exist.")
        return True
    return False


def check_output_extension(output_path: str) -> str:
    """Check if the input and output file paths have the correct extension.

    If either the input or output path does not end with '.json',it returns a modified output path.

    Args:
    ----
        output_path (str): Path of the output file.

    Returns:
    -------
        str: Base output path if the extension is correct.
        str: Modified output path if the extension is incorrect, otherwise the input output path.
    """
    _, out_extension = os.path.splitext(output_path)

    if out_extension != ".json":
        output_directory, _ = os.path.split(output_path)
        return os.path.join(output_directory, "default_output.json")

    return output_path


def check_input_extension(input_path: str) -> bool:
    """Check if the input file path has the correct extension.

    If the input path does not end with '.json', it returns True, indicating an error.

    Args:
    ----
        input_path (str): Path of the input file.

    Returns:
    -------
        bool: True if the extension is incorrect, otherwise False.
    """
    _, input_extension = os.path.splitext(input_path)

    if input_extension != ".json":
        handle_error("Input file does not have the correct extension.")
        return True
    return False


def check_errors(input_path: str, output_path: str) -> bool:
    """Check for errors in the input file.

    Args:
    ----
        input_path (str): Path of the input file.
        output_path (str): Path of the input file.

    Returns:
    -------
        bool: True if there are errors, otherwise False.
    """
    return (
        check_input_extension(input_path) or
        check_path(input_path, output_path) or
        is_file_empty(input_path)
        )
