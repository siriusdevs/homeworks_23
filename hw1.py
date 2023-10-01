"""Home work about company's salary."""


def salary_info(
    *args: tuple[str, dict[str, float]],
    arg: tuple[str] | None = None,
) -> list[str]:
    """Find top 3 salaries and a top salaries sum to all salaries ratio.

    Args:
        args: tuple[str, dict[str, float]] - company departments, employees and their salaries.
        arg: tuple[str] - exculded company.

    Returns:
        list[str] - top 3 salaries and the ratio for each company.
    """
    answer = []
    for index, _ in enumerate(args):
        list_of_values = []
        incident = arg if arg else []
        if args[index][0] not in incident:
            for values_of_salary in args[index][1].values():
                list_of_values.append(values_of_salary)
            list_of_values = sorted(list_of_values)
            all_our_arr = list_of_values[:1] + list_of_values[1:2]
            sum_of_our_salary = sum(all_our_arr + list_of_values[2:3])
            sum_of_all_salary = sum(list_of_values)
            answer.append(
                '1: {0:.2f}, '.format(sum(list_of_values[:1]))
                + '2: {0:.2f}, '.format(sum(list_of_values[1:2]))
                + '3: {0:.2f}; '.format(sum(list_of_values[2:3]))
                + '{0:.2f}%'.format(sum_of_our_salary / (sum_of_all_salary or 1) * 100),
            )
    return answer
