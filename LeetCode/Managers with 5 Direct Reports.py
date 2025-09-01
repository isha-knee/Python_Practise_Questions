Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
#If managerId is null, then the employee does not have a manager. No employee will be the manager of themself.
Write a solution to find managers with at least five direct reports.
Return the result table in any order.

  import pandas as pd
  def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    total= employee.groupby('managerId')['id'].count()
    managers=total[total>=5].index
    result=employee.loc[employee['id'].isin(managers),['name']]
    return result
