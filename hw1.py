"""Function for calculate statistic."""


def company(*departments: tuple[str, dict[str, float]],
            limit: float | None = None):
    """
    Calculates average salaries for each department
    and identifies the top 3 best-paid and worst-paid departments based on the average salary.

    Args:
        *departments (tuple[str, dict[str, float]]):
        Tuples with department name and employee salaries.
        limit (float | None):
        Optional salary limit for department consideration.

    Returns:
        dict: Dictionary with keys "best_paid" and "worst_paid"
        listing the top 3 departments in each category.
    """

    dict_average_sal_per_dep = {}
    list_salaries_per_dep = []

    for div in departments:
        number_of_emp = 0
        average = 0
        for salary in div[1].values():
            number_of_emp += 1
            average += salary
        average = round(average / number_of_emp, 2)

        if isinstance(limit, float):
            if average < limit:
                dict_average_sal_per_dep[div[0]] = average
                list_salaries_per_dep.append(average)
        else:
            dict_average_sal_per_dep[div[0]] = average
            list_salaries_per_dep.append(average)

    list_salaries_per_dep.sort()

    top_3_worst_sals = list_salaries_per_dep[0:3]
    top_3_best_sal = list_salaries_per_dep[-3:]

    best = []
    worst = []

    for dep_name, average_sal in dict_average_sal_per_dep.items():
        if average_sal in top_3_best_sal:
            best.append(dep_name)
        elif average_sal in top_3_worst_sals:
            worst.append(dep_name)

    response = {"best_paid": best,
                "worst_paid": worst}
    return response
