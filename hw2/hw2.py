import json, os
from typing import Any
from datetime import date, datetime
from statistics import mean

class PathError(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f'File with path: "{path}" is not exist')

class ExtentionError(Exception):
    def __init__(self, extention: str, expected: str) -> None:
        super().__init__(f'File must be {expected}, but got {extention}')

def open_json(path_to_file: str) -> dict[str:dict[str:Any]]:
    if not os.path.isfile(path_to_file):
        raise PathError(path_to_file)
    
    extention = os.path.splitext(path_to_file)[1]
    if not extention == '.json':
        raise ExtentionError(extention, '.json')
    
    with open(path_to_file) as file:
        data = json.load(file)

    return data

def count_email_domain(json_file: dict[str:dict[str:Any]]) -> dict:
    users = json_file.keys()
    amount_of_users = len(users)
    email_statistics = {}

    for user in users:
        email = json_file[user]['email'].split('@')[1]

        if not email in email_statistics.keys():
            email_statistics[email] = 1
        else:
            email_statistics[email] += 1
    
    for mail in email_statistics.keys():
        percent = round(email_statistics[mail] / amount_of_users * 100, 2)
        email_statistics[mail] = f'{percent}%'

    return email_statistics

def count_user_age(json_file: dict[str:dict[str:Any]]) -> dict:
    current_date = datetime.now()
    users = json_file.keys()
    time_steps = {'Less than 2 days': 2,
                  'Less than a week': 7,
                  'Less than a month': 31,
                  'Less than half a year': 186}
    
    average_age = {time_lapse: [] for time_lapse in time_steps.keys()}
    average_age['More than half a year'] = []

    for user in users:
        age = json_file[user]['age']
        last_login = datetime.strptime(json_file[user]['last_login'], '%Y-%m-%d')
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
    