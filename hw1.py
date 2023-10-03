"""This is main code for first homework."""
from typing import Tuple

test_data = {
    'it':{
        'Bob':1450.5,
        'Jeremy':999.9,
        'Elijah':1000,
        'Charlie':150.45
    },
    'marketing':{
        'Rimus':1500,
        'Thomas':1250.5,
        'Richard':79893.12312,
        'Charlie':150.45
    },
    'managment':{
        'Elon':99999999999.99999999,
        'Tim':100,
    },
}


def get_salary_stats(data: dict, department: str, limit: int = None) -> Tuple:
    """This function works with salaries data.
    
    
    Args:
        data: dictionary of dictionaries that includes departments and salaries data,
        department: string that tells us which department we are looking for,
        limir: default is None, sets up limit for salary, everything above is ignored.
    
    Returns:
        tuple: tuple with top 3 salaries and ratio of this 3 salaries to all of them in department.
        
    """
    data_raw = data[department]
    salaries_list = data_raw.values()
    sum_salaries = sum(salaries_list)
    if limit != None:
        salaries_list = [x for x in salaries_list if x <= limit]
    salaries = []
    for elem in salaries_list:
        salaries.append(elem)
    for salary in salaries:
        salaries.remove(salary)
        salary = round(salary, 2)
        salaries.append(salary)
    salaries = sorted(salaries, reverse = True)
    ratio = round((sum(salaries[:3]) / sum_salaries) * 100, 2) 
    out = ()
    out += (tuple(salaries[:3]))
    return out, ratio
