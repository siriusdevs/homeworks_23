"""This modile include function get_statistic."""


from typing import Optional


def get_statistic(departamen_data: dict, limit: Optional[int] = None) -> tuple:
    """Take a dictionary with salary as input and return statistics.

    Args:
        departamen_data: dictionary with the names departments as keys,\
            the dictionary with employee names as keys\
            and salaries as values
        limit: A numerical limit above which salaries need not be taken

    Returns:
        A tuple with average, maximum and median salary.
    """
    salary_people = []
    for names_departamens in departamen_data.keys():
        for salary in departamen_data[names_departamens].values():
            salary_people.append(salary)

    salary_people = sorted(
        filter(lambda se: limit is None or se <= limit, salary_people),
    )

    if not salary_people:
        return (0, 0, 0)
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
