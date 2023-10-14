"""Модуль для расчёта статистики."""
# Модуль для расчёта статистики: топ-3 самых
# высокооплачиваемых отдела в компании и топ-3 самых
# низкооплачиваемых (по средней зарплате в отделе).


def salary_statistics(
    exclude_department: tuple[str] = None,
        **department: dict[str: dict[str, float]],
) -> tuple[list]:
    """Вывод топ-3 высокооплачиваемых отделов и топ-3 низкооплачиваемых отделов в компании.

    Args:
        exclude_department (tuple[str]): Кортеж названий отделов(str), которые нужно
            исключить из статистики. По умолчанию None.
        department (dict[str: dict[str, float]]): словарь, где название отдела ключи(str),
            а другой словарь значение(dict), где имена сотрудников отдела ключи(str),
                а зарплаты значение(float).

    Returns:
        Tuple[list]: статистика топ-3 самых высокооплачиваемых отдела в компании
        и топ-3 самых низкооплачиваемых.

    Raises:
        Exception: выдает ошибку, когда в отделе нет сотрудников.
    """
    average_salaries = []

    for dep in department.keys():
        len_dep = len(department[dep])
        if len_dep == 0:
            raise Exception(f'В отделе {dep} нет сотрудников!')
        if exclude_department is None or dep not in exclude_department:
            average_salary = round(sum(department[dep].values()) / len_dep, 2)
            average_salaries.append([dep, average_salary])

    average_salaries.sort(key=lambda depart: depart[1])
    top_dep = [depart[0] for depart in average_salaries[-3:]]
    worst_dep = [depart[0] for depart in average_salaries[:3]]

    return top_dep, worst_dep
