# Dataset-for-Climate-Change-Tweets

The repository contains dataset consists of climate change tweets along with the annotations for the stance and sentiment of the tweet.
Stance of the tweet is identified using a label propagation algorithm (). Sentiment of the tweet is identified using majority voting of the three classifiers: 

The repository consists of the following files:
1. dataset.csv: is a ";" separated file that contains tweet ids, sentiment label(positive/negative/neutral) and stance label(believe/deny)
2. tweet_ids.txt: contains the tweet ids of all the collected tweets.
3. fetch_tweet.py: python script to collect the tweet object as it is not allowed to share the tweet text publicly.
