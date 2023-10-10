"""Функция для генерации отчетов о самых высокооплачиваемых и самых низкооплачиваемых отделах."""
import statistics


def check_arguments(departments: tuple) -> None:
    """Функция для проверки на пригодность переданных аргументов.

    Args:
        departments: tuple - кортеж кортежей с информацией об отделах в компании

    Raises:
        AttributeError: Ошибка связанная с некорректно переданными в функцию аргументы
    """
    if not departments:
        raise AttributeError(
            'Недостаточно аргументов для анализа.'
            +
            '\nТребуется ввести информацию минимум об 1 отделе!',
            )

    for department in departments:
        if len(department) != 2:
            raise AttributeError(
                'Некорректно передана информация об отделах'
                +
                '\nКортеж должен содержать 2 элемента: Название отдела и список с зарплатами!!!',
            )

        if not department[1]:
            raise AttributeError(
                f'Для отдела "{department[0]}" некорректно переданы зарплаты.'
                +
                '\nВ отделе должен числиться минимум 1 сотрудник!',
                )


def generete_report(*departments: tuple, exceptions: tuple = None) -> tuple:
    """Анализирует аргументы и возвращает топ 3 высокооплачиваемых и самых низкооплачиваемых отдела.

    Args:
        departments: tuple - Название отдела и список зарплат сотрудников
        exceptions: tuple - Кортеж с названиями отделов, которые нужно исключить из отчета

    Returns:
        tuple - кортеж из 2 списков: Топ 3 высокооплачиваемых отдела и топ 3 низкооплачиваемых
    """

    def sort_data(department: tuple, reverse: bool) -> list:
        updated_data = sorted(department, key=lambda dpt: statistics.mean(dpt[1]), reverse=reverse)
        return [department[0] for department in updated_data if department[0] not in exceptions]

    check_arguments(departments)

    if not exceptions:
        exceptions = ()

    higest = sort_data(departments, reverse=True)
    lowest = sort_data(departments, reverse=False)

    return lowest[:3], higest[:3]
