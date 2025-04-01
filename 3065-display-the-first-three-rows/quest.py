import pandas as pd

def createBonusColumnss(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.salary * 2
    return employees