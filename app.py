# -*- coding: utf-8 -*-
import tweepy
import config
import json
import codecs

def gettweets():
	auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
	auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	querys = ['Messi','sogaz','Bundesliga','BVB','SNF','premierleague']
	langs=["en","ru","de"]
	max_tweets = 200
	for lang in langs:
		for query in querys:
			searched_tweets = [status for status in tweepy.Cursor(api.search, q=query,lang=lang).items(max_tweets)]
			for tweetin in searched_tweets:
				tweet = json.loads(json.dumps(tweetin._json))
				ret={}
				try:
					if (not tweet["text"].find("RT")) or  (not tweet["entities"]["hashtags"]):
						continue
					ret["tweet_url"]=tweet["entities"]["urls"][0]["url"]
					ret["expanded_url"]=tweet["entities"]["urls"][0]["expanded_url"]
					hashtags=[]
					for hashtag in tweet["entities"]["hashtags"]:
						hashtags.append(hashtag["text"])
					ret['hashtags']=hashtags
					ret["created_at"]=tweet["created_at"]
					ret["text"]=tweet["text"].replace('\n',' ').replace('\r',' ')
					ret["lang"]=tweet["lang"]
				except Exception as e:
					pass
				else:
					with codecs.open("tweets4.json", "a") as stream:
						data=json.dumps(ret,ensure_ascii=False)
						stream.write(str(data)+'\n')
gettweets()