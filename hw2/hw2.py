"""Модуль для вывода статистики сайта."""
import json
from datetime import datetime


def process_data(
    input_path: str = 'data_hw2.json', output_path: str = 'data_result.json'
):
    """
    Функция реализующая анализ существующего json и соберет из него новую статистику.

    Args:
        input_path (str): путь, где находится .json файл.
        output_path (str): путь для записи итогового .json файла.
    """
    with open(input_path, 'r') as input_file:
        data = json.load(input_file)

    regions = {}
    ages = []
    last_login_dates = []

    for user, user_info in data.items():
        region = user_info['region']
        age = user_info['age']
        last_login = datetime.strptime(user_info['last_login'], '%Y-%m-%d')

        if region not in regions:
            regions[region] = 0
        regions[region] += 1

        ages.append(age)
        last_login_dates.append(last_login)

    total_users = len(data)

    region_distribution = {
        region: (count / total_users) * 100 for region, count in regions.items()
    }

    average_age = sum(ages) / total_users

    online_times = [datetime.now() - date for date in last_login_dates]
    online_days = [time.total_seconds() / (60 * 60 * 24) for time in online_times]

    stats = {
        'region_distribution': region_distribution,
        'average_age': average_age,
        'online_times': {
            '<2 days': sum(day < 2 for day in online_days) / total_users,
            '<1 week': sum(day < 7 for day in online_days) / total_users,
            '<1 month': sum(day < 30 for day in online_days) / total_users,
            '<6 months': sum(day < 180 for day in online_days) / total_users,
            '>6 months': sum(day > 180 for day in online_days) / total_users,
        },
    }

    with open(output_path, 'w') as output_file:
        json.dump(stats, output_file)


process_data()
