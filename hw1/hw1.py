def salary_statistics(company_dict, min_salary=None):
    """salary statictics function.

    Args:
        company_dict: dict - a dictionary with company departments and workers.
        min_salary: int optional - the minimum threshold for salaries. Defaults to None.

    Returns:
        dict: - output data.
    """
    # создаём список со всеми зп
    all_salaries = []
    for key in company_dict:
        workers = company_dict[key]

        all_salaries.extend(workers.values())

    if min_salary is not None:
        # если есть аргумент min_salary отсеиваем всё, что меньше его
        all_salaries = list(filter(lambda x: x >= min_salary, all_salaries))

    # топ 3 зп
    top_salaries = sorted(all_salaries, reverse=True)[0:3]

    for i in range(3):
        top_salaries[i] = round(top_salaries[i], 2)

    # отношение топа зарплат ко всем
    ratio = round(sum(top_salaries) / sum(all_salaries) * 100, 2)

    return {'top': top_salaries, 'ratio': ratio}
