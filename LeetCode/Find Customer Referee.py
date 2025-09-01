Table: Customer
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
Find the names of the customer that are either:
referred by any customer with id != 2.
not referred by any customer.
Return the result table in any order.
The result format is in the following example.

import pandas as pd
def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
     mask= (customer['referee_id']!=2) | (customer['referee_id'].isnull())
     result= customer.loc[mask,['name']]
     return result
