"""Модуль для получения статистики о последнем входе."""


from datetime import date

SIX_MONTHS = 182
MONTHS = 30
WAS_ONLINE = 'было в сети менее'
msg_tuple = (
    (1, f'{WAS_ONLINE} недели назад'),
    (6, f'{WAS_ONLINE} месяца назад'),
    (MONTHS, f'{WAS_ONLINE} полугода назад'),
    (SIX_MONTHS, 'было в сети более полугода назад'),
)


def get_last_login(day: int) -> str:
    """Получить статистику когда был последний вход.

    Args:
        day (int): количество дней

    Returns:
        str: сообщение о том когда был последний вход
    """
    msg = f'{WAS_ONLINE} 2 дней назад'
    for current in msg_tuple:
        if day > current[0]:
            msg = current[1]
        else:
            break

    return msg


def find_was_online(last_logins: list) -> dict:
    """Получить статистику последнего входа.

    Args:
        last_logins (list): даты последнего входа

    Returns:
        dict: словарь со статистикой последнего входа
    """
    static = {}
    today = date.today()
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
