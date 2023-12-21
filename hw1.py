"""Top 3 departments module."""


def calculate_salary_stats(
    *departments: tuple[str, list[float]],
    salary_limit: float | None = None,
) -> tuple[list[float], float]:
    """
    Find 3 most paid salaries and the ratio of the amount \
            of this top to the entire amount of payments in the company in a given tuple.

    Args:
        departments: tuple with departments names their values.
        salary_limit: the maximum wage value (float) to be taken into account.

    Returns:
        stats: tuple of 3 most paid salaries and the ratio of the amount \
            of this top to the entire amount of payments in the company.
    """
    all_salaries = []

    for _, salaries in departments:
        for salary in salaries:
            if salary_limit is None or salary >= salary_limit:
                all_salaries.append(round(salary, 2))

    all_salaries = sorted(all_salaries, reverse=True)

    top = all_salaries[:3]
    percant_top = sum(top) / sum(all_salaries) * 100 if all_salaries else 0
    return top, round(percant_top, 2)
