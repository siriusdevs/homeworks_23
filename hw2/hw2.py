"""This is a solution of hw2.

Напишите модуль,
в котором функция process_data принимает путь к json-файлу с данными о клиентах сайта
(пример файла в data_hw2.json)
и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику:
процент аудитории каждой возрастной категории 0-18-25-45-60+,
а также процент регистраций пользователей по годам.
Вынести домашнее и его тесты в отдельную папку hw2.
Тесты используют различные json-файлы.
В workflows выделить отдельные работы для проверок линтера разных домашних,
отдельные работы для тестов разных домашних
(цель состоит в том, чтобы в actions они отображались отдельными галочками).
"""
import json

LOWEST_ADULT_AGE = 18
MIDDLE_ADULT_AGE = 25
LOWEST_ADULT_PLUS_AGE = 45
HIGHEST_ADULT_PLUS_AGE = 60


def stats_by_age(ages: list[int]) -> dict[str, float]:
    """Block that finds percentage of each age gap.

    Args:
        ages: list[int] with int values of ages that were given.

    Returns:
        output - dict:
            key: str with age-gap naming.
            value: float with percentage count of this age group.

    """
    output = {'Below 18': 0, '18 to 25': 0, '25 to 45': 0, '45 to 60': 0, 'Above 60': 0}
    age_gaps = [0, 0, 0, 0, 0]
    for age in ages:
        match age:
            case age if age < LOWEST_ADULT_AGE:
                age_gaps[0] += 1
            case age if age in range(LOWEST_ADULT_AGE, MIDDLE_ADULT_AGE):
                age_gaps[1] += 1
            case age if age in range(MIDDLE_ADULT_AGE, LOWEST_ADULT_PLUS_AGE):
                age_gaps[2] += 1
            case age if age in range(LOWEST_ADULT_PLUS_AGE, HIGHEST_ADULT_PLUS_AGE):
                age_gaps[3] += 1
            case age if age > HIGHEST_ADULT_PLUS_AGE:
                age_gaps[4] += 1
    total = sum(age_gaps)
    if age_gaps == 0:
        return output
    temp = [
        round(age_gaps[0] / total * 100, 2),
        round(age_gaps[1] / total * 100, 2),
        round(age_gaps[2] / total * 100, 2),
        round(age_gaps[3] / total * 100, 2),
        round(age_gaps[4] / total * 100, 2),
        ]
    for index, age_gap in enumerate(output.keys()):
        output[age_gap] = temp[index]
    return output


def count_unique(sample: list[str]) -> dict[str, float]:
    """Counter of unique elements in list.

    Args:
        sample: list of str elemetns.

    Returns:
        dict:
            key: str with name of unique element.
            value: float with count percentage of it on file.

    """
    output = {}
    for element in sample:
        if element not in output.keys():
            output.update({element: 1})
        else:
            output[element] += 1
    total = sum(output.values())
    if total == 0:
        return output.update({'No values were found': 0})
    for key in output.keys():
        output[key] = round(output[key] / total * 100, 2)
    return output


def process_data(in_path: str, out_path: str) -> None:
    """Block that is sollution for hw2.

    Args:
        in_path: str, that contains path to input .json file.
        out_path: str, that contains path to output .json file.

    Raises:
        ValueError: if given path to file leads to nothing or empty file.
    """
    try:
        with open(in_path) as inputdata:
            user_stats = json.load(inputdata)
    except json.JSONDecodeError:
        raise ValueError('File that you provided is empty, not valid or not exists')
    with open(in_path) as input_data:
        user_stats = json.load(input_data)
    ages = []
    reg_years = []
    for user_data in user_stats.values():
        ages.append(user_data['age'])
        reg_years.append(user_data['registered'][:4])
    with open(out_path, 'w') as json_file:
        json.dump(
            {'Registration stats': count_unique(reg_years)} |
            {'Age-gaps stats': stats_by_age(ages)},
            fp=json_file,
                )
