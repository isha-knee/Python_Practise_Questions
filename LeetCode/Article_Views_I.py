Table: Views
#Note that equal author_id and viewer_id indicate the same person.
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
#Write a solution to find all the authors that viewed at least one of their own articles. Return the result table sorted by id in ascending order.
import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result= (views.loc[views['author_id']== views['viewer_id'], ['author_id']]
    .drop_duplicates()
    .sort_values('author_id',ascending=True)
    .rename(columns={'author_id': 'id'}))
    return result
