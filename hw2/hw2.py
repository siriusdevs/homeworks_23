"""Function that calculates website usage statistics.

Напишите модуль, в котором функция process_data принимает путь к json-файлу
с данными о клиентах сайта (пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику: процент использования
каждого почтового хоста в почтах клиентов, а также средний возраст клиентов,
которые были онлайн менее двух дней, недели, месяца, полугода, и более полугода назад.
Вынести домашнее и его тесты в отдельную папку hw2. Тесты используют различные json-файлы.
В workflows выделить отдельные работы для проверок линтера разных домашних,
отдельные работы для тестов разных домашних
(цель состоит в том, чтобы в actions они отображались отдельными галочками).
"""
import json
from datetime import datetime

MONTH = 30
HALF_YEAR = 180

LESS_THAN_TWO_DAYS = 'less_than_2_days'
LESS_THAN_ONE_WEEK = 'less_than_1_week'
LESS_THAN_ONE_MONTH = 'less_than_1_month'
LESS_THAN_SIX_MONTHS = 'less_than_6_months'
MORE_THAN_SIX_MONTHS = 'more_than_6_months'

EMAIL_USAGE = 'email_usage'
TIME_STATS = 'time_stats'


def stats_by_time(information: dict) -> dict[str, list]:
    """Dictributes age over time.

    Args:
        information: dict - information of users.

    Returns:
        time_stats: dict - dict about users sorted by time.

    """
    time_stats = {
        LESS_THAN_TWO_DAYS: [],
        LESS_THAN_ONE_WEEK: [],
        LESS_THAN_ONE_MONTH: [],
        LESS_THAN_SIX_MONTHS: [],
        MORE_THAN_SIX_MONTHS: [],
    }
    for user_info in information.values():
        age = user_info.get('age')
        online = datetime.now() - datetime.strptime(user_info.get('last_login'), '%Y-%m-%d')

        match online.days:
            case online.days if online.days <= 2:
                time_stats[LESS_THAN_TWO_DAYS].append(age)
            case online.days if online.days <= 7:
                time_stats[LESS_THAN_ONE_WEEK].append(age)
            case online.days if online.days <= MONTH:
                time_stats[LESS_THAN_ONE_MONTH].append(age)
            case online.days if online.days <= HALF_YEAR:
                time_stats[LESS_THAN_SIX_MONTHS].append(age)
            case online.days if online.days > HALF_YEAR:
                time_stats[MORE_THAN_SIX_MONTHS].append(age)

    for time, quantity in time_stats.items():
        if quantity:
            time_stats[time] = sum(quantity) / len(quantity)
        else:
            time_stats[time] = 0
    return time_stats


def stats_by_email(information: dict) -> dict[str, int]:
    """Check that email is email.

    Args:
        information: dict - information of users.

    Returns:
        mail_host: dict - dict about users sorted by email.

    """
    mail_host = {}
    for user_info in information.values():
        email: str = user_info.get('email')
        if email:
            email_parts = email.split('@')
            if len(email_parts) == 2:
                if email_parts[1] not in mail_host.keys():
                    mail_host[email_parts[1]] = 1
                else:
                    mail_host[email_parts[1]] += 1
    return mail_host


def write_to_output(file_name: str, msg: str) -> None:
    """Write message in file.

    Args:
        file_name: str - the name of file where we write
        msg: str - message we write in file

    """
    with open(file_name, 'w') as output:
        json.dump(msg, output)


def process_data(input_data, output_data):
    """Calculate websites usage statistics.

    Args:
        input_data: name of the input data file.
        output_data: name of the output data file.

    """
    try:
        with open(input_data) as input_file:
            information: dict[str, dict] = json.load(input_file)
    except json.JSONDecodeError:
        write_to_output(output_data, 'Input file was empty')
        return
    except FileNotFoundError:
        write_to_output(output_data, 'Input file was not given')
        return

    mail_host = stats_by_email(information)
    time_stats = stats_by_time(information)

    stats: dict[str, dict[str, list]] = {
        EMAIL_USAGE: mail_host,
        TIME_STATS: time_stats,
        }

    with open(output_data, 'w') as output_file:
        json.dump(stats, output_file, indent=4, ensure_ascii=False)


process_data('data_hw2.json', 'output_test.json')
