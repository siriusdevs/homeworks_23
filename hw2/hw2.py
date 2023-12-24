import json


def process_data(input_path, output_path):
    """a function that processes json with users.

    Args:
        input_path: str -  the path to the input data file.
        output_path: str - the path to the output file.
    """
    with open(input_path, 'r') as read_file:
        # получаем данные из json
        data = json.load(read_file)

    # получаем возраст каждого пользователя
    ages = [user['age'] for user in data.values()]

    # словарь со статистикой зарегистрировавшихся пользователей по годам
    years = {}

    for user in data.values():
        year = user['registered'].split('-')[0]
        years[year] = years.get(year, 0) + 1

    for key in years:
        # переводим в проценты
        years[key] = int(years[key] / len(data) * 100)

    with open(output_path, 'w') as write_file:
        # пишем в выходной json файл
        write_file.write(json.dumps({
            'min_age': min(ages),
            'max_age': max(ages),
            'middle_age': sum(ages) // len(ages),
            'mediana': max(ages, key=lambda k: ages.count(k))
        }))
        write_file.write(json.dumps(years))
