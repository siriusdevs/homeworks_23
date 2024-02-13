"""A module that accepts clients input data and an output result.

Напишите модуль, в котором функция process_data принимает путь к json-файлу
с данными о клиентах сайта
(пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику:
процент распределения географии пользователей по городам,
а также процент клиентов, которые были онлайн:
менее двух дней, недели, месяца, полугода, и более полугода назад.
Вынести домашнее и его тесты в отдельную папку hw2.
Тесты используют различные json-файлы.
В workflows выделить отдельные работы для проверок линтера разных домашних,
отдельные работы для тестов разных домашних
(цель состоит в том, чтобы в actions они отображались отдельными галочками).
"""
import json
import os

import extra


def process_data(input_path: str, output_path: str) -> None:
    """
    Collect the data from the clients, calculate statistics to the output path.

    If output file does not exist, then create a directory with JSON file.

    Args:
        input_path (str): The input path to JSON file with clients data.
        output_path (str): The output path to JSON file with statistics of the results.

    Raises:
        ValueError: If JSON file is incorrect.
    """
    extra.check_paths(input_path, output_path)
    try:
        with open(input_path, 'r') as input_file:
            clients = json.load(input_file)
    except ValueError:
        raise ValueError('Input file is broken and not readable!')

    statistics = {
        'regions_stats': extra.process_regions(clients),
        'last_login_stats': extra.process_last_login(clients),
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as output_file:
        json.dump(statistics, output_file, indent=4)
