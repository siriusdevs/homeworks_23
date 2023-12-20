"""Calculate and return the top 3 salaries and their ratio to the total salary."""

def salary_stats(*departments, limit=None):
    """
    Calculate and return the top 3 salaries and their ratio to the total salary.

    Args:
        departments (tuple): Variable length tuple containing department name and list of salaries.
        limit (float, optional): Limit below which salaries shouldnt be considered. Default None.

    Returns:
        tuple: Tuple containing list of top 3 salaries and their ratio to the total salary.
    """
    all_salaries = []
    for department, salaries in departments:
        if limit is not None:
            salaries = [salary for salary in salaries if salary > limit]
        all_salaries.extend(salaries)

    all_salaries.sort()
    top_salaries = all_salaries[:3]
    total_salary = sum(all_salaries)
    try:
        top_ratio = sum(top_salaries) / total_salary * 100
    except ZeroDivisionError:
        top_ratio = 0

    return [round(salary, 2) for salary in top_salaries], round(top_ratio, 2)
