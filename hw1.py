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
    top_salaries = []
    if required_deps:
        departments = filter(lambda arg: arg, departments)
        departments = filter(lambda arg: arg[0] in required_deps, departments)
        departments = tuple(departments)
    required_salaries = [salaries[1] for salaries in departments if len(salaries) > 1]
    for salaries in required_salaries:
        top_salaries.extend(salaries)
    if any(salary < 0 for salary in top_salaries):
        return 'Sorry, salary cannot be less than zero.'
    top_salaries.sort(reverse=True)
    try:
        percent = sum(top_salaries[:3]) / sum(top_salaries) * 100
    except ZeroDivisionError:
        if top_salaries:
            percent = float(100)
        else:
            percent = float(0)
    return top_salaries[:3], round(percent, 2)
