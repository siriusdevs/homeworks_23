from typing import TypeAlias, Sequence


def get_median(items: Sequence[float | int]) -> float:
    length = len(items)
    centre_index = (length - 1) // 2

    if length == 0:
        return 0.0

    if length % 2 == 1:
        return float(items[centre_index])

    return (items[centre_index] + items[centre_index + 1]) / 2


MinSalary: TypeAlias = None | int | float
Employees: TypeAlias = dict[str, float]  # name, salary
Companies: TypeAlias = dict[str, Employees]  # company name, employees dictionary

CompanyStatistic: TypeAlias = tuple[float, float, float]  # average, maximum and median salary
CompaniesStatistic: TypeAlias = dict[str, CompanyStatistic]  # company name, company statistic


def calculate_companies_statistic(min_salary: MinSalary = None, **companies: Companies) \
        -> CompaniesStatistic:

    result: CompaniesStatistic = dict()

    for company_name, employees in companies.items():
        salary_sum = 0
        max_salary = 0
        filtered_salaries: list[float] = list()

        for salary in employees.values():
            if min_salary is not None and salary < min_salary:
                continue

            salary_sum += salary
            max_salary = salary if max_salary < salary else max_salary
            filtered_salaries.append(salary)

        salaries_length = len(filtered_salaries)
        average = salary_sum / salaries_length if salaries_length > 0 else 0
        median = get_median(filtered_salaries)

        total = tuple(round(salary, 2) for salary in [average, max_salary, median])
        result[company_name] = total

    return result


print(calculate_companies_statistic(apple={
    'a': 100,
    'b': 300,
    'c': 500,
    'df': 348,
}, samsung={
    'dkfj': 577,
}, hi={}))
