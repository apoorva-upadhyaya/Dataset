import tweepy
import json
import pandas as pd


CONSUMER_KEY="" 
CONSUMER_SECRET=""
OAUTH_TOKEN=""
OAUTH_TOKEN_SECRET=""


list_ids=[]
with open("tweet_ids.txt",'r',encoding='utf-8') as file:
		for line in file:
			file=""
			line=line.rstrip()
			id_=line
			list_ids.append(id_)

print("len of tweets",len(list_ids))




auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

count=0
for single_id in list_ids:
	#print(type(single_id))
	
	try:		
		tweet=api.get_status(single_id, tweet_mode='extended')
		count=count+1
		print(count)
		#<convert <class 'tweepy.models.Status'> to string representation of dict>
		json_str = json.dumps(tweet._json)
		#<convert string representation of dict to dict>
		tweet=json.loads(json_str)
		with open("tweets.json","a") as f:
			json.dump(tweet,f)
			f.write("\n")
	except Exception as e:
		print("e ::",e)
		continue
