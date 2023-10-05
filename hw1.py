"""Module for salary analysis and calculations."""


def get_top_salaries(*departments: tuple[str, list], required_deps: tuple[str] = None) -> tuple:
    """Get the 3 highest salaries and the ratio of their sum to the sum of all salaries.

    Args:
        departments: Tuple[str, list] - departments name and lists of salaries.
        required_deps: Tuple[str] - names of departments in which salaries need to be calculated.

    Returns:
        tuple: two elements:
        - A list of the top three salaries (sorted in descending order).
        - The percentage that the top three salaries contribute to the total
        salaries within the specified departments, rounded to two decimal places.
    """
    sorted_salaries = []
    if required_deps:
        departments = filter(lambda arg: arg, departments)
        departments = filter(lambda arg: arg[0] in required_deps, departments)
        departments = tuple(departments)
    for department in departments:
        if len(department) > 1:
            sorted_salaries.extend(department[1])
    if any(salary < 0 for salary in sorted_salaries):
        return 'Sorry, salary cannot be less than zero.'
    sorted_salaries.sort()
    try:
        percent = sum(sorted_salaries[:3]) / sum(sorted_salaries) * 100
    except ZeroDivisionError:
        if sorted_salaries:
            percent = float(100)
        else:
            percent = float(0)
    return sorted_salaries[:3], round(percent, 2)


print(get_top_salaries(('Develop', [20, 20, 20, 80, 20]), ('Marketing', [20, 20, 20, 80, 20]), ('Sales', [20, 20, 20, 80, 20])))
