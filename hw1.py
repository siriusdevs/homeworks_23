"""Module that includes the implemented function from Nudga's first task."""


from typing import Optional, Tuple


def sort_dep(*args: Tuple[str, int], limit: Optional[int] = None) -> Tuple[str]:
    """
    Create a function that sorts a tuple of departments.

    Args:
        args: Tuple[str, int] - Department name and employee salary.
        limit: Optional[int] - Payroll accounting limit in sorting.

    Returns:
        Return Tuple[str]
    """
    if limit is not None:
        filtered_args = [
            (dept, [salary for salary in salaries if salary >= limit])
            for dept, salaries in args
            ]
    else:
        filtered_args = args

    filtered_args = [
        (dept, salaries)
        for dept, salaries in filtered_args
        if sum(salaries) > 0
        ]

    if not filtered_args:
        return (), ()

    sorted_args = sorted(
        filtered_args,
        key=lambda dept: sum(dept[1]) / len(dept[1]),
        reverse=True,
        )

    top3_high = [dept for dept, _ in sorted_args[:3]]
    top3_low = [dept for dept, _ in sorted_args[-3:]]
    return top3_high, top3_low
