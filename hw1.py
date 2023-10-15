"""Module that includes the implemented function from Nudga's first task."""


from typing import Optional


def sort_dep(*departments: tuple[str, list[int|float]] , limit: Optional[float] = None) -> tuple[str, str]:
    """
    Create a function that sorts a tuple of company.

    Args:
        departments: tuple[str, list[int|float]] - Department name and employee salary.
        limit: Optional[float] - Payroll accounting limit in sorting.

    Returns:
        Return tuple[str, str] - Top 3 high-paying and low-paying departments.
    """
    if limit is not None:
        filtered_dep = [
            (dept, [salary for salary in salaries if salary >= limit])
            for dept, salaries in departments
            if any(salary >= limit for salary in salaries)
        ]

    else:
        filtered_dep = departments
    if not filtered_dep:
        return (), ()

    filtered_dep = sorted(
        filtered_dep,
        key=lambda dept: sum(dept[1]) / len(dept[1]),
        reverse=True,
        )

    top3_high = [dept for dept, _ in filtered_dep[:3]]
    top3_low = [
        dept
        for dept, _ in filtered_dep[-1:-4:-1]
        ]
    return top3_high, top3_low
