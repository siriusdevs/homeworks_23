"""Function calculates top 3 salaries and their sum percentage of all salaries."""
from typing import Any, Optional


def check_type(
    input_value: Any, types: tuple[type, ...] | type,
    check_positive: Optional[bool] = False,
) -> None:
    """
    Check if value is of type `types`.

    Args:
        input_value (Any): The value to check.
        types (tuple[type, ...]): The type to check against.
        check_positive (Optional[bool], optional): Check if value is positive. Defaults to False.

    Raises:
        TypeError: If value is not of type `types`.
        ValueError: If value is not positive.
    """
    if not isinstance(input_value, types):
        value_type = type(input_value)
        error_msg = f'Expected type {types}, got {value_type}'
        raise TypeError(error_msg)
    if check_positive and input_value < 0:
        raise ValueError(f'Expected positive value, but got {input_value}')


def salary_stat(
    *args: tuple[str, list[float]],
    exclude: Optional[tuple[str]] = None,
) -> tuple[list[float], float]:
    """Return top 3 salaries and their sum percentage of all salaries.

    Args:
        args: tuple[str, list[float]]: department name and list of salaries.
        exclude: Optional[tuple[str]]: departments to exclude.

    Returns:
        tuple[list[float], float]: top 3 salaries and their sum percentage.
    """
    if exclude is None:
        exclude = ()
    else:
        exclude = set(exclude)

    salaries = []
    for department, department_salaries in args:
        if exclude is None or department not in exclude:
            for salary in department_salaries:
                check_type(salary, float, check_positive=True)
            salaries.extend(department_salaries)
    salaries.sort(reverse=True)
    top_salaries = salaries[:3]
    top_salaries_sum = sum(top_salaries)
    try:
        top_salaries_sum_percentage = top_salaries_sum / sum(salaries) * 100
    except ZeroDivisionError:
        top_salaries_sum_percentage = 0
    return top_salaries, round(top_salaries_sum_percentage, 2)
