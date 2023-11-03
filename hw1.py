from itertools import chain


def check_arguments(departments: dict[str, dict], limit_salary: int | float):
    if not departments:
        raise ValueError('No one argument in departments')

    for department, workers in departments.items():
        if not isinstance(department, str) or not isinstance(workers, dict):
            raise TypeError('Wrong type of department or workers')

        for worker, salary in workers.items():
            if not isinstance(worker, str) or not isinstance(salary, float):
                raise TypeError('Wrong type of worker or salary')

    if limit_salary and not isinstance(limit_salary, (int, float)):
        raise TypeError(f'Optional argument limit_salary must be int or float, '
                        f'but got {type(limit_salary).__name__}')


def top_salary(
    limit_salary: int | float = None,
    **departments: dict[str, dict]
) -> (list[float], float):
    check_arguments(departments, limit_salary)

    all_salaries = sorted(list(chain.from_iterable(workers.values() for workers in
                                                   departments.values())), reverse=True)

    if limit_salary:
        top = list(filter(lambda x: x < limit_salary, all_salaries))[:3]
    else:
        top = all_salaries[:3]

    percent = round(sum(top) / sum(all_salaries) * 100, 2)

    return [round(salary, 2) for salary in top], percent
