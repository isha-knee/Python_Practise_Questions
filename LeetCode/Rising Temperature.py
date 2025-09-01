Table: Weather
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
Return the result table in any order.

import pandas as pd
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather= weather.assign(prev_temp=weather['temperature'].shift(1))
    mask= weather['temperature']> weather['prev_temp']
    result= weather.loc[mask,['id']].rename(columns={'id':'Id'})
    return result
  #Or you can also use this method:
import pandas as pd
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    mask = weather['temperature'] > weather['temperature'].shift(1)
    result = weather.loc[mask, ['id']]
    result.columns = ['Id']
    return result
