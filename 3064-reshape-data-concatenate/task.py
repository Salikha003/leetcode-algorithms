import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


import pandas as pd

def selectSecondRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)