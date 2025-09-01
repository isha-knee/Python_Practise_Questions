Table: Tweets
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
Write a solution to find the IDs of the invalid tweets. 
The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
Return the result table in any order.

  import pandas as pd
  def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
     mask = tweets['content'].str.len() > 15
     return tweets.loc[mask, ['tweet_id']]
