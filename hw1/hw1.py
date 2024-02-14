"""Solution for hw1."""


def salary_statistics(company_dict: dict, min_salary: int = None) -> dict:
    """Salary statictics function.

    Args:
        company_dict: dict - a dictionary with company departments and workers.
        min_salary: float optional - the minimum threshold for salaries. Defaults to None.

    Returns:
        dict: - output data.
    """
    # создаём список со всеми зп
    all_salaries = []
    for workers in company_dict.values():
        all_salaries.extend(workers.values())

    if min_salary is not None:
        # если есть аргумент min_salary отсеиваем всё, что меньше его
        all_salaries = list(
            filter(lambda sal: sal >= min_salary, all_salaries))

    # топ 3 зп
    top_salaries = sorted(all_salaries, reverse=True)[:3]

    for ind, _ in enumerate(top_salaries):
        top_salaries[ind] = round(top_salaries[ind], 2)

    # отношение топа зарплат ко всем
    ratio = 0

    if all_salaries:
        ratio = round(sum(top_salaries) / sum(all_salaries) * 100, 2)

    return {'top': top_salaries, 'ratio': ratio}
