"""Top 3 salaries module."""


def top3_salaries_stats(
        departments: dict[str, float | int],
        excluding: tuple = None,
    ) -> tuple[tuple[str, float | int], tuple[str, float | int]]:
    """Find 3 most-paid and 3 least-paid departments in a given dictionary by average value.

    Args:
        departments: a dictionary with departments names (keys: str) and names of employees with their salaries (values: dict)
        excluding: tuple with names of departments to be excluded from stats, defaults to None

    Returns:
        stats: tuple of top 3 most and least paid departments with their average salaries.
    """
    if excluding is None:
        excluding = ()

    avg_salaries = {}
    for department, employees in departments.items():
        if department not in excluding:
            salaries = [salary for salary in employees.values()]
            if sum(salaries) == 0:
                avg_salary = 0
            else:
                avg_salary = round(sum(salaries) / len(salaries), 2)
            avg_salaries[department] = avg_salary

    top3_most_paid = sorted(avg_salaries.items(), key=lambda x: x[1], reverse=True)[:3]
    top3_least_paid = sorted(avg_salaries.items(), key=lambda x: x[1])[:3]
    return tuple(top3_most_paid), tuple(top3_least_paid)

#

test_dep = {
        'Drivers': {'Dennis': 1000.0, 'Ivan': 100.0, 'Alex': 0},
        'Bodyguards': {'Andrew': 2000.0, 'Vladislav': 100.0, 'Vitaliy': 900.0},
        }

print(top3_salaries_stats(test_dep))