"""Модуль для получения статистики о последнем входе."""


from datetime import date

SIX_MONTHS = 182
MONTHS = 30


def get_last_login(day: int):
    """Получить статистику когда был последний вход.

    Args:
        day (int): количество дней

    Returns:
        str: сообщение о том когда был последний вход
    """
    if day > SIX_MONTHS:
        msg = 'было в сети более полугода назад'
    elif day > MONTHS:
        msg = 'было в сети менее полугода назад'
    elif day > 6:
        msg = 'было в сети менее месяца назад'
    elif day > 1:
        msg = 'было в сети менее недели назад'
    else:
        msg = 'было в сети менее 2 дней назад'

    return msg


def find_was_online(last_logins: list):
    """Получить статистику последнего входа.

    Args:
        last_logins (list): даты последнего входа

    Returns:
        dict: словарь со статистикой последнего входа
    """
    static = {}
    today = date.fromisoformat('2023-12-10')
    for last_login in last_logins:
        last_login = date.fromisoformat(last_login)
        day = (today - last_login).days
        msg = get_last_login(day)
        if msg in static.keys():
            static[msg] += 1
        else:
            static[msg] = 1
    for key in static.keys():
        percent = round(static[key] / len(last_logins) * 100)
        static[key] = f'{percent}%'
    return static
