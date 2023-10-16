"""Top 3 salaries module."""


def top3_salaries_stats(
    departments: dict[str, float | int],
    excluding: tuple[str, ...] = None,
    ) -> tuple[
    tuple[str, float | int],
    tuple[str, float | int]
    ]:
    """Find 3 most- and least-paid departments in a given dictionary by average value.

    Args:
        departments: a dictionary with departments names their values.
        excluding: tuple with names of departments to be excluded from stats, defaults to None.

    Returns:
        stats: tuple of top 3 most and least paid departments with their average salaries.
    """

    avg_salaries = {}
    for department, employees in departments.items():
        if excluding is None or department not in excluding:
            salaries = [salary for salary in employees.values()]
            if sum(salaries) == 0:
                avg_salary = 0
            else:
                avg_salary = round(sum(salaries) / len(salaries), 2)
            avg_salaries[department] = avg_salary

    top3_most_paid = sorted(avg_salaries.items(), key=lambda srt: srt[1], reverse=True)[:3]
    top3_least_paid = sorted(avg_salaries.items(), key=lambda srt: srt[1])[:3]
    return tuple(top3_most_paid), tuple(top3_least_paid)
