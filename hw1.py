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

    Raises:
        Exception: occurs if there are salaries less than zero.
    """
    required_salaries = []
    if required_deps:
        departments = filter(lambda arg: arg, departments)
        departments = tuple(filter(lambda arg: arg[0] in required_deps, departments))
    for department in departments:
        if len(department) > 1:
            required_salaries.extend(department[1])
    if any(salary < 0 for salary in required_salaries):
        raise Exception('Sorry, salary cannot be less than zero.')
    required_salaries.sort()
    try:
        percent = sum(required_salaries[:3]) / sum(required_salaries) * 100
    except ZeroDivisionError:
        percent = float(100) if required_salaries else float(0)
    return required_salaries[:3], round(percent, 2)
