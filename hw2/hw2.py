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
import os
import os.path as op

LOWEST_ADULT_AGE = 18
MIDDLE_ADULT_AGE = 25
LOWEST_ADULT_PLUS_AGE = 45
HIGHEST_ADULT_PLUS_AGE = 60

BELOW_LA_AGE_STRING = 'Below 18'
LA_TO_MA_AGE_STRING = '18 to 25'
MA_TO_LAP_AGE_STRING = '25 to 45'
LAP_TO_HAP_AGE_STRING = '45 to 60'
HIGHEST_AND_ABOVE_AP_AGE_STRING = 'Above 60'
UNDEFINED_AGE_STRING = 'Undefined'


def stats_by_age(ages: list[int]) -> dict[str, float]:
    """Block that finds percentage of each age gap.

    Args:
        ages: list[int] with int values of ages that were given.

    Returns:
        output - dict:
            key: str with age-gap naming.
            value: float with percentage count of this age group.

    Raises:
        ValueError: if age that given is not number

    """
    output = {
        BELOW_LA_AGE_STRING: 0,
        LA_TO_MA_AGE_STRING: 0,
        MA_TO_LAP_AGE_STRING: 0,
        LAP_TO_HAP_AGE_STRING: 0,
        HIGHEST_AND_ABOVE_AP_AGE_STRING: 0,
        UNDEFINED_AGE_STRING: 0,
        }
    for age in ages:
        if not isinstance(age, (int, float)):
            raise ValueError(f'{age} was given instead of proper numeric age')
        match age:
            case age if age in range(0, LOWEST_ADULT_AGE):
                output[BELOW_LA_AGE_STRING] += 1
            case age if age in range(LOWEST_ADULT_AGE, MIDDLE_ADULT_AGE):
                output[LA_TO_MA_AGE_STRING] += 1
            case age if age in range(MIDDLE_ADULT_AGE, LOWEST_ADULT_PLUS_AGE):
                output[MA_TO_LAP_AGE_STRING] += 1
            case age if age in range(LOWEST_ADULT_PLUS_AGE, HIGHEST_ADULT_PLUS_AGE):
                output[LAP_TO_HAP_AGE_STRING] += 1
            case age if age >= HIGHEST_ADULT_PLUS_AGE:
                output[HIGHEST_AND_ABOVE_AP_AGE_STRING] += 1
            case age if not age:
                output[UNDEFINED_AGE_STRING] += 1

    total = sum(output.values())
    if total == 0:
        return output
    temp = [
        round(output[BELOW_LA_AGE_STRING] / total * 100, 2),
        round(output[LA_TO_MA_AGE_STRING] / total * 100, 2),
        round(output[MA_TO_LAP_AGE_STRING] / total * 100, 2),
        round(output[LAP_TO_HAP_AGE_STRING] / total * 100, 2),
        round(output[HIGHEST_AND_ABOVE_AP_AGE_STRING] / total * 100, 2),
        round(output[UNDEFINED_AGE_STRING] / total * 100, 2),
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
            output[element] = 1
        else:
            output[element] += 1
    total = sum(output.values())
    if total == 0:
        return output.update({'No values were found': 0})
    for key in output.keys():
        output[key] = round(output[key] / total * 100, 2)
    return output


def write_to_file(
    file_path: str,
    reg_years: list[str],
    ages: list[int],
    error_flag: bool = False,
        ) -> None:
    """Output writer module.

    Args:
        error_flag: bool value that tells us to add or not add error in output file.
        file_path: path to file that we need to write output to.
        reg_years: list of different registration years from given json.
        ages: list of ages that we generate from given json.

    """
    if error_flag:
        with open(file_path, 'w') as j_err_file:
            json.dump(
                {'File Error, there are some troubles with given file': None},
                fp=j_err_file,
            )
        return
    if op.dirname(file_path) and not op.exists(file_path):
        os.makedirs(op.dirname(file_path))
    with open(file_path, 'w') as json_file:
        json.dump(
            {'Registration stats': count_unique(reg_years)}
            | {'Age-gaps stats': stats_by_age(ages)},
            fp=json_file,
        )


def process_data(in_path: str, out_path: str) -> None:
    """Block that is sollution for hw2.

    Args:
        in_path: str, that contains path to input .json file.
        out_path: str, that contains path to output .json file.

    """
    try:
        with open(in_path) as inputdata:
            user_stats = json.load(inputdata)
    except json.JSONDecodeError:
        write_to_file(out_path, [], [], error_flag=True)
        return
    except FileNotFoundError:
        write_to_file(out_path, [], [], error_flag=True)
        return
    except PermissionError:
        write_to_file(out_path, [], [], error_flag=True)
        return
    ages = []
    reg_years = []
    for user_data in user_stats.values():
        if 'age' not in user_data.keys():
            user_data.update({'age': None})
        elif 'registered' not in user_data.keys():
            user_data.update({'registered': 'NaN'})
        ages.append(user_data['age'])
        reg_years.append(user_data['registered'][:4])
    write_to_file(out_path, reg_years, ages)
