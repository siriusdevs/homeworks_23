"""Module for salary analysis and calculations."""


def get_top_salaries(*args: tuple[str, list], departments: tuple[str] = None) -> tuple:
    """Get the 3 highest salaries and the ratio of their sum to the sum of all salaries.

    Args:
        args: Tuple[str, list] - departments name and lists of salaries.
        departments: Tuple[str] - names of departments in which salaries need to be calculated.

    Returns:
        tuple: A tuple containing two elements:
        - A list of the top three salaries (sorted in descending order).
        - The percentage that the top three salaries contribute to the total
        salaries within the specified departments, rounded to two decimal places.
    """
    top_salaries = []
    if departments:
        args = filter(lambda arg: arg, args)
        args = filter(lambda arg: arg[0] in departments, args)
        args = tuple(args)
    required_salaries = [salaries[1] for salaries in args if len(salaries) > 1]
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
