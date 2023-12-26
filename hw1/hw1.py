"""Module for calculating salary statistics."""


def salary_statistics(company_dict, min_salary=None):
    """Salary statictics function.

    Args:
        company_dict: dict - a dictionary with company departments and workers.
        min_salary: int|float optional - the minimum threshold for salaries. Defaults to None.

    Returns:
        dict: - output data.
    """
    # создаём список со всеми зп
    all_salaries = []
    for workers in company_dict.values():
        all_salaries.extend(workers.values())

    if min_salary is not None:
        # если есть аргумент min_salary отсеиваем всё, что меньше его
        all_salaries = list(filter(lambda fltr: fltr >= min_salary, all_salaries))

    # топ 3 зп
    top_salaries = sorted(all_salaries, reverse=True)[:3]

    for top in range(3):
        top_salaries[top] = round(top_salaries[top], 2)

    # отношение топа зарплат ко всем
    if sum(all_salaries) > 0:
        ratio = round(sum(top_salaries) / sum(all_salaries) * 100, 2)
    else:
        ratio = 0
    return {'top': top_salaries, 'ratio': ratio}
