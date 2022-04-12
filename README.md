# Dataset-for-Climate-Change-Tweets

The repository contains a dataset of tweets about climate change along with the stance and sentiment annotations of the tweet.

The **stance** of the tweet is identified using a label propagation algorithm (_Tyagi, A., Babcock, M., Carley, K.M. and Sicker, D.C., 2020, October. Polarizing tweets on climate change. In International Conference on Social Computing, Behavioral-Cultural Modeling and Prediction and Behavior Representation in Modeling and Simulation (pp. 107-117). Springer, Cham._). 
The **sentiment** of the tweet is determined by a majority vote of the three classifiers: (i) _VADER:_ is a popular lexicon and rule-based sentiment analysis tool that relies on a dictionary to generate sentiment scores, (ii) _TextBlob_ (https://textblob.readthedocs.io/en/dev/): is a Python-based library that provides an API for handling common NLP tasks such as sentiment analysis, POS tagging, etc., and (iii) _NLTK_ (https://www.nltk.org/index.html): is a Python bundle that provides a collection of NLP algorithms like sentiment analysis, NER, etc.

The repository consists of the following files:
1. dataset.csv: is a ";" separated file that contains tweet ids, sentiment label (positive/negative/neutral) and stance label (believe/deny ).
2. tweet_ids.txt: contains the tweet ids of all collected tweets.
3. fetch_tweets.py: Python script to collect the tweet object, as it is not allowed to share the tweet text publicly.
