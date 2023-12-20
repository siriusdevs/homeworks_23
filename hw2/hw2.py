"""Process json data."""
# Напишите модуль, (U ᵕ U❁) в котором
# функция pwocess_data принимает путь к json-файлу
# с данными о клиентах сайта (пример файла в
# data_hw2.json) и путь к j-json-файлу вывода. (⑅˘꒳˘)
# Функция p-pwocess_data записывает в этот общий
# j-json статистику: процент распределения
# географии пользователей по городам, ( ͡o ω ͡o )
# а также средний возраст клиентов, UwU которые
# были онлайн менее двух дней, rawr x3 недели, rawr
# месяца, σωσ полугода, σωσ и более полугода
# назад. >_< Вынести домашнее и его тесты в
# отдельную папку h-hw2. :3 Тесты используют
# различные j-json-файлы. (U ﹏ U) В w-wowkfwows выделить
# отдельные работы для проверок линтера разных
# домашних, -.- отдельные работы для тестов
# разных домашних (цель состоит в том, (ˆ ﻌ ˆ)♡
# чтобы в a-actions они отображались отдельными
# галочками). (⑅˘꒳˘)

import json
import os
import shutil
from datetime import datetime, timedelta
from types import MappingProxyType

CURR_DATE = datetime.today()

# You can change more or less than the time period by writing lt or gt respectivly
TIME_RANGES = MappingProxyType({
    'lt_2_days':  2,
    'lt_week':  7,
    'lt_month':  30,
    'lt_half_year':  182,
    'gt_half_year': 182,
})

AGE = 'age'
LAST_LOGIN = 'last_login'
REGION = 'region'

AGE_STATS = 'age_stats'
REGION_STATS = 'region_stats'

OVERWRITE_FILES = False


def _convert_time_ranges(time_ranges: MappingProxyType) -> dict:
    ranges = {}
    for range_, days in time_ranges.items():
        ranges[range_] = timedelta(days=days)

    return ranges


def _get_json(inpath: str) -> dict:
    with open(inpath, 'r') as infile:
        users = json.load(infile)

    if not isinstance(users, dict):
        raise ValueError('Given a json of type {0}, but dict is needed'.format(
            users.__class__.__name__,
        ))

    return users


def _dump_json(outpath: str, output: dict) -> None:
    dirs = outpath.rfind('/')
    if dirs > -1 and not os.path.isdir(outpath[:dirs]):
        os.makedirs(outpath[:dirs])

    if OVERWRITE_FILES is False and os.path.exists(outpath):
        shutil.move(outpath, '{0}-old'.format(outpath))

    with open(outpath, 'w') as outfile:
        json.dump(output, outfile, indent=4)


def _combine_results(ages: dict, cities: dict) -> dict:
    output = {
        AGE_STATS: {},
        REGION_STATS: {},
    }

    for span, age in ages.items():
        non_zero_age = max(len(age), 1)
        output[AGE_STATS][span] = round(sum(age) / non_zero_age, 2)

    for reg, num in cities.items():
        output[REGION_STATS][reg] = round(num / len(cities), 2)

    return output


def convert_date(date: str) -> datetime:
    """
    Convert a date string to a datetime object.

    Args:
        date (str): The date string to be converted.

    Returns:
        datetime: The converted datetime object.
    """
    return datetime.strptime(date, '%Y-%m-%d')


def av_user_age(user: dict, age: dict) -> dict:
    """
    Update the age dict with the user's age if the user's last login is within the time ranges.

    Args:
        user (dict): The user dictionary containing the user's details.
        age (dict): The age dictionary to be updated.

    Returns:
        dict: The updated age dictionary.
    """
    if not age:
        age = {scope: [] for scope in TIME_RANGES.keys()}

    for scope, dur in _convert_time_ranges(TIME_RANGES).items():
        date_diff = CURR_DATE - convert_date(user[LAST_LOGIN])

        if scope.startswith('gt') and date_diff >= dur:
            age[scope].append(user[AGE])

        elif scope.startswith('lt') and date_diff <= dur:
            age[scope].append(user[AGE])

    return age


def process_data(inpath: str, outpath: str) -> None:
    """
    Process the user data from the input path and dumps the results to the output path.

    Args:
        inpath (str): The path to the input JSON file containing the user data.
        outpath (str): The path to the output JSON file where the results will be dumped.
    """
    users = _get_json(inpath)

    ages = {}
    cities = {user[REGION]: 1 for user in users.values()}

    for user in users.values():
        ages.update(av_user_age(user, ages))
        cities[user[REGION]] += 1

    _dump_json(outpath, _combine_results(ages, cities))
