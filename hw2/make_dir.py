"""Module for making dirs."""
import os


def make_dir(output_file):
    """Initialize the path.

    Args:
        output_file (str): file for stats
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
