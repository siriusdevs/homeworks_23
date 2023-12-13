import json

def process_data(input: str, output: str):

    users = get_users_from_json(input)

    ages = [user['age'] for user in users.values()]

    min_age = min(ages)
    max_age = max(ages)
    avg_age = int(sum(ages) / len(ages))
    
    median_age = get_median_age(ages)

    stats = get_years_statistic(users)

    r = json.dumps({"minimum_age" : min_age, "maximum_age" : max_age,"average_age" : avg_age, "mediian_age" : median_age, "statistic" :stats})
    print(r)
    

def get_users_from_json(path: str) -> dict:
    with open(path) as file:
        return json.load(file)
            
    
def get_years_statistic(users: list[dict]):
    all_count = len(users)
    stats = {}
    for user in users.values():
        date = user['registered']
        stats[date] = stats.get(date, 0) + 1

    stats = {year: ratio(count, all_count) for year, count in stats.items()}
    
    return stats

def ratio(figure: int|float, to_figure: int|float):
    return round(figure / to_figure * 100, 2)

def get_median_age(ages: list[int]) -> int:

    sort_ages = sorted(ages)
    len_ages = len(sort_ages)
    half_len_ages = len_ages // 2

    if len_ages % 2 == 0:
        return (sort_ages[half_len_ages] +  sort_ages[half_len_ages - 1]) // 2
    else:
        return sort_ages[half_len_ages]

process_data("data_hw2.json", "")
