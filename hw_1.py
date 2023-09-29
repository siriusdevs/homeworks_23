from dataclasses import dataclass 

@dataclass 
class SalaryStats: 
    average: float 
    median: float
    maximum: float 

def get_salary_stats() -> SalaryStats: 
    pass
