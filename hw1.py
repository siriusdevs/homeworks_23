"""Top 3 departments module."""


def salary_statistics(
    *departments: tuple[str, list[float]],
    salary_limit: float | None = None,
) -> tuple[list]:
    """Find three most- and least-paid departments in a given tuple by average value.

    Args:
        departments: tuple with departments names their values.
        salary_limit: the maximum wage value (float) to be taken into account.

    Returns:
        stats: tuple of top 3 most and least paid departments with their average salaries.
    """
    filtered = {}
    for department, salaries in departments:
        salaries = [
            salary for salary in salaries if salary_limit is None or salary <= salary_limit
        ]
        filtered[department] = round(sum(salaries) / len(salaries), 2) if salaries else .0

    filtered = sorted(
        filtered.items(),
        key=lambda department_info: department_info[1],
        reverse=True,
    )
    return filtered[:3], filtered[-3:]
