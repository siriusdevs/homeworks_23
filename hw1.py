"""Calculates top and bottom three salaries."""


from typing import Dict, Tuple


def top_three_salaries(
    names: Tuple[str, ...] | None = None,
    **kwargs: Dict[str, float],
) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    """
    Extract top and bottom three salaries.

    Args:
        names: Tuple[str, ...] | None - Optional tuple of names for return.
        kwargs: Dict[str, int] - dict of department names and their values.

    Returns:
        Tuple[Tuple[float, ...], Tuple[float, ...]] - inner tuples are with lowest and
        highest salaries
    """
    avgs = []
    for elem in kwargs.keys():
        if names is None or elem in names:
            cur_elem = kwargs[elem].values()
            cur_avg = sum(cur_elem) / max(len(cur_elem), 1)
            avgs.append([elem, cur_avg])

    avgs.sort(key=lambda department: department[1])
    lowest = [low[0] for low in avgs[:3]]
    highest = [high[0] for high in avgs[-3:]]
    return tuple(lowest), tuple(highest)
