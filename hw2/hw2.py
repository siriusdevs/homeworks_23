"""
Provides types and functions for solving task_2.

Напишите модуль, в котором функция process_data принимает путь к json-файлу с данными
о клиентах сайта (пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику:
минимальный, максимальный, средний и медианный возраст пользователя, а также средний возраст
клиентов, которые были онлайн менее двух дней, недели, месяца, полугода, и более полугода назад.
"""


def aggregate_users_stats(input_file: str, output_file: str) -> None:
    """Read user stats from input_file, aggregate them and write to output_file.

    Args:
        input_file: path to a json file containing user stats
        output_file: path to an output file. json aggregate stats will be written there.
    """
    pass
