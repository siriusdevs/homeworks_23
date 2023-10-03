"""Module for salary analysis and calculations."""

from typing import Tuple


def get_top_salaries(*args: Tuple[str, list], departments: Tuple[str] = None) -> tuple:
    """Get the 3 highest salaries and the ratio of their sum to the sum of all salaries.

    Args:
        args: Tuple[str, list] - departments name and lists of salaries.
        departments: Tuple[str] - names of departments in which salaries need to be calculated.

    Returns:
        tuple: A tuple containing two elements:
        - A list of the top three salaries (sorted in descending order).
        - The percentage that the top three salaries contribute to the total
        salaries within the specified departments, rounded to two decimal places.
    """
    top_salaries = []
    if departments:
        args = tuple(filter(lambda arg: arg[0] in departments, args))
    required_salaries = [salaries[1] for salaries in args]
    for salaries in required_salaries:
        top_salaries.extend(salaries)
    top_salaries.sort(reverse=True)
    try:
        percent = sum(top_salaries[:3]) / sum(top_salaries) * 100
    except ZeroDivisionError:
        if top_salaries:
            percent = float(100)
        else:
            percent = float(0)
    return top_salaries[:3], round(percent, 2)

print(get_top_salaries(('', [20])))
