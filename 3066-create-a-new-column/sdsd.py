import pandas as pd

def createBonusColumnqqq(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.salary * 2
    return employees