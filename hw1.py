"""This is the main code for first homework."""


def get_salary_stats(
    company_salaries_data: dict[str, dict],
    limit: int = None,
) -> tuple:
    r"""Block of code that is designed to search for top 3 salaries in chosen department and etc.

    Args:
        company_salaries_data: dictionary of dictionaries that includes departments and salaries.
        limit: default is None, sets up limit for salary, everything above is ignored.

    Returns:
        tuple: tuple with top 3 salaries and ratio of them to all salaries in department \
            or tuple with zeros if there is no salary in company.

    """
    salaries = []
    for departments in company_salaries_data.values():
        salaries_list = departments.values()
        if limit:
            salaries_list = [salary for salary in salaries_list if salary <= limit]
        salaries += salaries_list
    salaries = sorted([round(salary, 2) for salary in salaries], reverse=True)
    top3salariessum = round(sum(salaries[:3]), 2)
    if sum(salaries) == 0:
        return (0, 0, 0), 100
    ratio = (top3salariessum / sum(salaries)) * 100
    return tuple(salaries[:3]), round(ratio, 2)
