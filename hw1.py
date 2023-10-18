"""Module for calculating the lowest 3 salaries and their part of all payments."""

# Напишите функцию, которая принимает любое количество позиционных аргументов,
# где каждый аргумент - это кортеж формата
# ((название отдела компании(str),
# {словарь фамилий сотрудников этого отдела(str) и их зарплат(float)]).
# Функция должна возвращать статистику:
# последние 3 зарплат в компании(по размеру),
# отношение суммы этих 3 зарплат ко всему размеру выплат в компании, в процентах.
# Функция также должна принимать опциональный аргумент, который по умолчанию равен None.
# Этот аргумент - числовой предел, выше которого зарплаты учитывать не нужно.
# Все числа в выводе функции округлять до второго знака после запятой.


def calculate_lowest_salaries(
    *company: tuple[str, dict],
    salary_limit: int = None,
) -> tuple[list[float], str]:
    """Calculate lowest salaries and their ratio to all payments.

    Args:
        company: tuple of tuples with company department name, \
            and dictionary of surnames of employees and their salaries.
        salary_limit: numerical limit above which salaries should not be taken.

    Returns:
        tuple: contains list of all employee salaries and \
            the percentage of three lowest salaries from all payments.
    """
    total_payments = 0
    salaries = []
    for _, employees in company:
        for salary in employees.values():
            if salary_limit is None or salary <= salary_limit:
                total_payments += salary
                salaries.append(round(salary, 2))

    if total_payments == 0:
        return [], '100%'

    lowest_salaries = sorted(salaries)[:3]
    ratio_lowest_salaries = round(sum(lowest_salaries) * 100 / total_payments)

    return lowest_salaries, f'{ratio_lowest_salaries}%'
