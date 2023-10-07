"""This is the main code for first homework."""


def get_salary_stats(data_salaries: dict, limit: int = None) -> tuple:
    """Block of code that is designed to search for top 3 salaries in chosen department and etc.

    Args:
        data_salaries: dictionary of dictionaries that includes departments and salaries data.
        limit: default is None, sets up limit for salary, everything above is ignored.

    Raises:
        ZeroDivisionError: if there are no salaries paid in company

    Returns:
        tuple: tuple with top 3 salaries and ratio of this 3 salaries to all of them in department.

    """
    salaries = []
    for department, _ in data_salaries.items():
        data_raw = data_salaries[department]
        salaries_list = data_raw.values()
        if limit:
            salaries_list = [salary for salary in salaries_list if salary <= limit]

        for salary in salaries_list:
            salaries.append(salary)
        salaries = [round(salary, 2) for salary in salaries]
        salaries = sorted(salaries, reverse=True)
        if sum(salaries) == 0:
            raise ZeroDivisionError('It seems like there is no salary at all, check the data')
        top3salariessum = round(sum(salaries[:3]), 2)
        ratio = (top3salariessum / sum(salaries)) * 100
    return tuple(salaries[:3]), round(ratio, 2)
