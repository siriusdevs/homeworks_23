import statistics
import json
import re


def process_data(input_path, output_path):
    """a function that processes json with users.

    Args:
        input_path: str -  the path to the input data file.
        output_path: str - the path to the output file.
    """
    try:
        with open(input_path, 'r') as file:
            # получаем данные из json
            data = json.load(read_file)

            # получаем возраст каждого пользователя
            ages = []
            for user in data.values():
                if "age" in user:
                    ages.append(user['age'])
                    
            # словарь со статистикой зарегистрировавшихся пользователей по годам
            years = {}

            for user in data.values():
                if 'registered' in user:
                    year = re.split(r"[-.]", user['registered'])[0]
                    years[year] = years.get(year, 0) + 1

            for key in years:
                # переводим в проценты
                years[key] = int(years[key] / len(data) * 100)

            if len(ages) > 0:
                with open(output_path, 'w') as write_file:
                    # пишем в выходной json файл
                    write_file.write(json.dumps({
                        'min_age': min(ages),
                        'max_age': max(ages),
                        'middle_age': sum(ages) // len(ages),
                        'mediana': statistics.median(ages)
                    }))
            else:
                print("Невозможно посчитать статистику для возрастов, так как список пуст")

            with open(output_path, 'w') as write_file:
                write_file.write(json.dumps(years))
        
    except FileNotFoundError:
        print(f"Файл '{input_path}' не найден.")
        return None
