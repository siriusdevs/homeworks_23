"""Module that includes the implemented function from Nudga's first task."""


from typing import Optional


def sort_dep(
    *departments: tuple[str, list[int | float]],
    limit: Optional[float] = None,
) -> tuple[list[str], list[str]]:
    """
    Create a function that sorts a tuple of company.

    Args:
        departments: tuple[str, list[int|float]] - Department name and employee salary.
        limit: Optional[float] - Payroll accounting limit in sorting.

    Returns:
        Return tuple[str, str] - Top 3 high-paying and low-paying departments.
    """
    filtered_dep = []
    for dept, salaries in departments:
        filtered_salaries = [
            salary for salary in salaries if salary >= limit
        ] if limit is not None else salaries

        if filtered_salaries:
            filtered_dep.append((dept, filtered_salaries))

    if not filtered_dep:
        return [], []

    filtered_dep = sorted(
        filtered_dep,
        key=lambda department: sum(department[1]) / len(department[1]),
        reverse=True,
    )

    top3_high = [department for department, _ in filtered_dep[:3]]
    top3_low = [
        department
        for department, _ in filtered_dep[-1:-4:-1]
    ]
    return top3_high, top3_low
