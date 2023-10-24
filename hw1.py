from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class SalaryStats:
    average: float = 0.0
    median: float = 0.0
    maximum: float = 0.0


def get_salary_stats(units: Optional[Tuple[str]] = None, **kwargs) -> SalaryStats:
    stats = SalaryStats()
    return stats
