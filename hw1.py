"""Top 3 departments by average salary."""
from typing import Dict, Optional, Tuple


def sort_key(dp: Tuple[str, Dict[str, float]]) -> float:
    """Key sorted for sorting departments.

    Args:
        dp (Tuple): a tuple containing the name of the company department, last name, salary.

    Raises:
        ValueError: departs_count must be more than zero.

    Returns:
        float: sum salaries.
    """
    departs_count = len(dp[1])
    if departs_count == 0:
        raise ValueError(f'{departs_count=} must be more than zero')
    return sum(list(dp[1].values())) / len(dp[1])


def top3(*args: Tuple[str, Dict[str, float]], sl_min: Optional[float] = None) -> list:
    """Return the top 3 departments by average salary.

    Args:
        args (Tuple): a tuple containing the name of the department, last name, salary.
        sl_min (int or None): mimimum salary limit.

    Raises:
        ValueError: sl_min must be float or int.

    Returns:
        list: departments.
    """
    if not sl_min:
        sl_min = 0
    if not isinstance(sl_min, float | int):
        raise ValueError(f'{sl_min=} sl_min must be float or int')

    departs = [list(dp) for dp in args]

    for num in range(int(len(departs))):
        names_sl = departs[num][1].keys(), departs[num][1].values()
        departs[num][1] = {}
        for name, sl in zip(names_sl[0], names_sl[1]):
            if sl >= sl_min:
                departs[num][1][name] = sl

    departs = sorted(departs, key=sort_key, reverse=True)

    first_three = [dp[0] for dp in departs[:3]]
    last_three = [dp[0] for dp in departs[:-4:-1]]
    return [first_three, last_three]
