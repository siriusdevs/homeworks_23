"""Модуль для вывода статистики сайта."""
import json
from datetime import datetime

MONTH = 30
HALF_YEAR = 180


def process_data(
    input_path: str = 'data_hw2.json',
    output_path: str = 'data_result.json'
):
    """
    Функция реализующая анализ существующего json и соберет из него новую статистику.

    Args:
        input_path (str): путь, где находится .json файл.
        output_path (str): путь для записи итогового .json файла.
    """
    with open(input_path, 'r') as input_file:
        json_data = json.load(input_file)

    regions = {}
    ages = []
    last_login_dates = []

    for user_info in json_data.items():
        last_login = datetime.strptime(user_info['last_login'], '%Y-%m-%d')

        if user_info['region'] not in regions:
            regions[user_info['region']] = 0
        regions[user_info['region']] += 1

        ages.append(user_info['age'])
        last_login_dates.append(last_login)

    total = len(json_data)
    region_distribution = {
        region: (count / total) * 100 for region, count in regions.items()
    }

    online_times = [datetime.now() - date for date in last_login_dates]
    online_days = [time.total_seconds() / (60 * 60 * 24) for time in online_times]

    stats = {
        'region_distribution': region_distribution,
        'average_age': sum(ages) / total,
        'online_times': {
            '<2 days': sum(day < 2 for day in online_days) / total,
            '<1 week': sum(day < 7 for day in online_days) / total,
            '<1 month': sum(day < MONTH for day in online_days) / total,
            '<6 months': sum(day < HALF_YEAR for day in online_days) / total,
            '>6 months': sum(day > HALF_YEAR for day in online_days) / total,
        },
    }

    with open(output_path, 'w') as output_file:
        json.dump(stats, output_file)


process_data()
