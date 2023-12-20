def salary_stats(*departments, limit=None):
    """
    Calculate and return the top 3 salaries and their ratio to the total salary.

    Args:
        departments (tuple): Variable length tuple containing department name and list of salaries.
        limit (float, optional): A limit below which salaries should not be considered. Defaults to None.

    Returns:
    list, .float: A list of top 3 salaries and their ratio to the total salary, both rounded to 2 decimal places.
    """
    all_salaries = []
    for department, salaries in departments:
        if limit is not None:
            salaries = [s for s in salaries if s > limit]
        all_salaries.extend(salaries)

    all_salaries.sort()
    top_3_salaries = all_salaries[:3]
    total_salary = sum(all_salaries)
    try:
        top_3_ratio = sum(top_3_salaries) / total_salary * 100
    except ZeroDivisionError:
        top_3_ratio = 0

    return [round(s, 2) for s in top_3_salaries], round(top_3_ratio, 2)
