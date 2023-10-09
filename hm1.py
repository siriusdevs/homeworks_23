"""Модуль для расчёта статистики."""
# Модуль для расчёта статистики: топ-3 самых
# высокооплачиваемых отдела в компании и топ-3 самых
# низкооплачиваемых (по средней зарплате в отделе).


def salary_statistics(exclude_department: tuple = None, **department: dict[str, float]) -> list:
    """Вывод топ-3 высокооплачиваемых отделов и топ-3 низкооплачиваемых отделов в компании.

    Args:
        exclude_department (tuple): Кортеж названий отделов, которые нужно
            исключить из статистики. По умолчанию None.
        department (dict[str, float]): словарь, где имена сотрудников отдела ключи(str),
            а зарплаты значение(float).

    Returns:
        list: статистика топ-3 самых высокооплачиваемых отдела в компании
        и топ-3 самых низкооплачиваемых.
    """
    average_salaries = []

    for dep in department.keys():
        len_dep = len(department[dep])
        if exclude_department is None or dep not in exclude_department:
            if len_dep > 0:
                average_salary = round(sum(department[dep].values()) / len_dep, 2)
                average_salaries.append([dep, average_salary])

    average_salaries = sorted(average_salaries, key=lambda depart: depart[1])
    top_dep = [depart[0] for depart in average_salaries[-3:]]
    worst_dep = [depart[0] for depart in average_salaries[:3]]

    return top_dep, worst_dep
