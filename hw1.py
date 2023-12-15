"""Top 3 salaries module."""


def top3_salaries(
    *args,
    including: tuple[str, ...] = None,
) -> tuple[tuple[str, float], tuple[str, float]]:
    """Find 3 most- and least-paid departments in a given tuple by average value.

    Args:
        departments: a tuple with departments names their values.
        excluding: tuple with names of departments to be excluded from stats, defaults to None.

    Returns:
        stats: tuple of top 3 most and least paid departments with their average salaries.
    """
    avg_salaries = {}
    for dept in args:
        department, workers = dept
        if including is None or department in including:
            salaries = workers.values()
            avg_salary = round(sum(salaries) / len(salaries), 2) if salaries else 0
            avg_salaries[department] = avg_salary

    salaries_sorted = sorted(avg_salaries.items(), key=lambda srt: srt[1], reverse=True)
    top3_most_paid = salaries_sorted[:3]
    top3_least_paid = salaries_sorted[-3:][::-1]
    return tuple(top3_most_paid), tuple(top3_least_paid)
