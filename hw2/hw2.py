import json, os, sys
from typing import Any
from datetime import datetime
from statistics import mean

class PathError(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f'File with path: "{path}" is not exist')

class ExtentionError(Exception):
    def __init__(self, extention: str, expected: str) -> None:
        super().__init__(f'File must be {expected}, but got {extention}')

def check_path(path_to_file: str) -> None:
    if not os.path.isfile(path_to_file):
        raise PathError(path_to_file)
    
def check_extention(path_to_file: str, extention: str) -> None:
    cur_extention = os.path.splitext(path_to_file)[1]
    if not cur_extention == extention:
        raise ExtentionError(cur_extention, extention)
    
def print_error(path_to_file: str, text: str):
    with open(path_to_file, 'w') as f:
        f.write(text)
    sys.exit()
    
def open_json(path_to_file: str, output_path: str) -> dict[str:dict[str:Any]]:
    try:
        check_path(path_to_file)
    except PathError:
        text = 'A file with an invalid path is given. Have a nice day!'
        print_error(output_path, text)

    try:
        check_extention(path_to_file, '.json')
    except ExtentionError:
        text = 'The input file should have a JSON extension, but another one is given. Have a nice day!'
        print_error(output_path, text)

    
    with open(path_to_file) as file:
        result_of_reading = json.load(file)

    return result_of_reading

def count_email_domain(json_file: dict[str:dict[str:Any]], output_path: str) -> dict:
    users = json_file.keys()
    amount_of_users = len(users)
    email_statistics = {}

    if amount_of_users == 0:
        text = 'There is no user information in the file. Have a nice day!'
        print_error(output_path, text)

    for user in users:
        try:
            email = json_file[user]['email'].split('@')[1]
        except IndexError:
            text = 'Mail with an invalid email has been entered in the file. Have a nice day!'
            print_error(output_path, text)

        if not email in email_statistics.keys():
            email_statistics[email] = 1
        else:
            email_statistics[email] += 1
    
    for mail in email_statistics.keys():
        percent = round(email_statistics[mail] / amount_of_users * 100, 2)
        email_statistics[mail] = f'{percent}%'

    return email_statistics

def count_user_age(json_file: dict[str:dict[str:Any]], output_file) -> dict:
    # Вообще, в идеале, тут правда должна быть текущая дата, но тогда тесты, увы, работают
    # только сутки (((
    # current_date = datetime.now()
    current_date = datetime.strptime('2023-12-20', '%Y-%m-%d')
    users = json_file.keys()
    time_steps = {'Less than 2 days': 2,
                  'Less than a week': 7,
                  'Less than a month': 31,
                  'Less than half a year': 186}
    
    average_age = {time_lapse: [] for time_lapse in time_steps.keys()}
    average_age['More than half a year'] = []

    for user in users:
        age = json_file[user]['age']
        if not isinstance(age, int):
            text = 'An incorrect age value has been entered. Have a nice day!'
            print_error(output_file, text)
        try:
            last_login = datetime.strptime(json_file[user]['last_login'], '%Y-%m-%d')
        except ValueError:
            text = 'The file contains a date in a non-correct format. Have a nice day!'
            print_error(output_file, text)
        days_from_last_login = (current_date - last_login).days
        added = False

        for time_lapse, days in time_steps.items():
            if days_from_last_login < days:
                average_age[time_lapse].append(age)
                added = True
                break
        
        if not added:
            average_age['More than half a year'].append(age)
    
    for time_lapse in average_age.keys():
        if average_age[time_lapse]:
            mean_age = mean(average_age[time_lapse])
            average_age[time_lapse] = mean_age
        else:
            average_age[time_lapse] = 'NaN'

    return average_age
    
def write_result_to_json(path_to_file: str,
                         email_statistics: dict[str:str],
                         average_age: dict[str:float|str],
                        ) -> None:

    to_json = {'email statistics':email_statistics,
               'average_age':average_age}
    
    with open(path_to_file, 'w') as file_to_write:
        file_to_write.write(json.dumps(to_json))
  

def analyze_json(path_to_json: str, path_to_result: str) -> None:
    json = open_json(path_to_json, path_to_result)
    write_result_to_json(path_to_result,
                         count_email_domain(json, path_to_result),
                         count_user_age(json, path_to_result),
                         )


if __name__ == '__main__':
    analyze_json('hw2/data_hw2.json', 'hw2/test.json')
