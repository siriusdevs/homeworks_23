"""This modile include function get_statistic."""


from typing import Optional


def get_statistic(department_data: dict[dict[float]], limit: Optional[int] = None) -> tuple[float]:
    """Take a dictionary with salary as input and return statistics.

    Args:
        department_data: dictionary with the names departments as keys,\
            the dictionary with employee names as keys\
            and salaries as values
        limit: A numerical limit above which salaries need not be taken

    Returns:
        A tuple with average, maximum and median salary.
    """
    salary_people = []
    for names_departments in department_data.values():
        for salary in names_departments.values():
            if limit is None or salary <= limit:
                salary_people.append(salary)

    if not salary_people:
        return (0, 0, 0)
    salary_people = sorted(salary_people)
    mal_salary = []
    len_salary_people = len(salary_people)

    if len_salary_people % 2 == 1:
        mal_salary.append(round(salary_people[len_salary_people // 2], 2))
    else:
        mal_salary.append(round(
            (salary_people[len_salary_people // 2] + salary_people[len_salary_people // 2 - 1]
             ) // 2, 2,
        ))
    mal_salary.append(round(max(salary_people), 2))
    mal_salary.append(round(sum(salary_people) / len_salary_people, 2))
    return tuple(mal_salary)
