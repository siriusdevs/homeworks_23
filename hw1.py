"""Функция для генерации отчетов о самых высокооплачиваемых и самых низкооплачиваемых отделах."""
import statistics


def check_arguments(departments: tuple[str, list[float]]) -> None:
    """Функция для проверки на пригодность переданных аргументов.

    Args:
        departments:
            tuple[str, list[float]] - кортеж, который содержит название отдела
            и список с зарплатами сотрудников отдела.

    Raises:
        AttributeError: Ошибка, связанная с некорректно переданными в функцию аргументами
    """
    if not departments:
        raise AttributeError(
            'Недостаточно аргументов для анализа.'
            +
            '\nТребуется ввести информацию минимум об 1 отделе',
            )

    for department in departments:
        if len(department) != 2:
            raise AttributeError(
                'Некорректно передана информация об отделах'
                +
                '\nКортеж должен содержать 2 элемента: Название отдела и список с зарплатами',
            )

        if not department[1]:
            raise AttributeError(
                f'Для отдела "{department[0]}" некорректно переданы зарплаты.'
                +
                '\nВ отделе должен числиться минимум 1 сотрудник',
                )


def generete_report(*departments: tuple[str, list[int | float]], 
                    exceptions: tuple[str] = None) -> tuple:
    """Анализирует аргументы и возвращает топ 3 высокооплачиваемых и самых низкооплачиваемых отдела.

    Args:
        departments:
            tuple[str, [int|float]] - Кортеж, содержащий название отдела и список с
            зарплатами сотрудников этого отдела
        exceptions:
            tuple[str] - Кортеж, содержащий названия отделов,
            которые будут исключены из результата работы функции.
            То есть не войдут в топ 3 высокооплачиваемых или низкооплачиваемых отдела.

    Returns:
        tuple[list[str], list] - кортеж из 2 списков:
        Топ 3 низкооплачиваемых отдела и топ 3 высокооплачиваемых соответственно
    """
    check_arguments(departments)
    exceptions = set() if exceptions is None else set(exceptions)

    new_data = sorted(departments, key=lambda dpt: statistics.mean(dpt[1]))
    # Меняю название переменной, чтобы линтер на длину строки не ругался
    sorted_deptmnt = [department[0] for department in new_data if department[0] not in exceptions]

    top_well_paid = sorted_deptmnt[:3]
    top_low_paid = sorted_deptmnt[-1:-4:-1]

    return top_well_paid, top_low_paid
