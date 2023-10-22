import json
import logging
import random
from datetime import date, datetime

from faker import Faker

TEST_FILES_DIR_PATH = 'hw2/test_files/input'
NOW = datetime.now()
REGIONS = ('Moscow', 'Sochi', 'Saint-Petersburg', 'New-York', 'Paris', 'London')

fake = Faker()


def get_random_date(start_year) -> date:
    year = random.randrange(start_year, NOW.year + 1)
    month = random.randrange(4, NOW.month + 1)
    day = random.randrange(1, NOW.day)

    result_date = date(year=year, month=month, day=day)
    return result_date


for i in range(1, 11):
    users = {}
    with open(f'{TEST_FILES_DIR_PATH}/{i}.json', 'w') as test_data_file:
        number_of_users = random.randrange(3, 11)
        for _ in range(number_of_users):
            region = random.choice(REGIONS)
            name = fake.name()
            email = fake.email()
            registered = get_random_date(start_year=2000)

            last_login = get_random_date(start_year=2023)
            while last_login <= registered:
                last_login = get_random_date(start_year=2023)

            users[name] = {
                'region': region,
                'registered': registered.__str__(),
                'last_login': last_login.__str__(),
                'email': email,
                'age': random.randrange(12, 78)
            }

        json.dump(users, test_data_file, indent=4, ensure_ascii=False)
