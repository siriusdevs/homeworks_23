"""This is a solution of hw2."""
import json
from json import JSONDecodeError

LOWEST_ADULT_AGE = 18
MIDDLE_ADULT_AGE = 25
LOWEST_ADULT_PLUS_AGE = 45
HIGHEST_ADULT_PLUS_AGE = 60


def stats_by_age(ages: list) -> dict:
    """Block that finds percentage of each age gap.

    Args:
        ages: list of ages that were given.

    Returns:
        dict: of age groups in percents.

    """
    output = {'Below 18': 0, '18 to 25': 0, '25 to 45': 0, '45 to 60': 0, 'Above 60': 0}
    younglings = 0
    padawans = 0
    adults = 0
    adults_plus = 0
    aged_people = 0
    for age in ages:
        match age:
            case age if age < LOWEST_ADULT_AGE:
                younglings += 1
            case age if age in range(LOWEST_ADULT_AGE, MIDDLE_ADULT_AGE):
                padawans += 1
            case age if age in range(MIDDLE_ADULT_AGE, LOWEST_ADULT_PLUS_AGE):
                adults += 1
            case age if age in range(LOWEST_ADULT_PLUS_AGE, HIGHEST_ADULT_PLUS_AGE):
                adults_plus += 1
            case age if age > HIGHEST_ADULT_PLUS_AGE:
                aged_people += 1
    total = younglings + padawans + adults + adults_plus + aged_people
    temp = [
        round(younglings / total * 100, 2), round(padawans / total * 100, 2),
        round(adults / total * 100, 2), round(adults_plus / total * 100, 2),
        round(aged_people / total * 100, 2),
        ]
    for index, age_gap in enumerate(output.keys()):
        output[age_gap] = temp[index]
    return output


def count_unique(sample: list) -> dict:
    """Counter of unique elements in list.

    Args:
        sample: list of elemetns.

    Returns:
        dict: where key is element and value it's percentage in list.

    """
    output = {}
    for element in sample:
        if element not in output.keys():
            output.update({element: 1})
        else:
            output[element] += 1
    total = sum(output.values())
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
    except JSONDecodeError:
        raise ValueError('File that you provided is empty')
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
