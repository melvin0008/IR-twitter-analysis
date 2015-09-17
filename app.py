# -*- coding: utf-8 -*-
import tweepy
import config
import json
import codecs

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, str):
        return input.replace('\\n',' ').encode("utf-8")
    else:
        return input

def gettweets():
	auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
	auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	# querys = ['ESPN','USL','UCL','Arsenal','Luke Shaw', 'LFC']
	# langs=["en","ru","de"]
	# max_tweets = 100
	# for lang in langs:
	# 	for query in querys:
	# 		searched_tweets = [status for status in tweepy.Cursor(api.search, q=query,lang=lang).items(max_tweets)]
	# 		for tweetin in set(searched_tweets):
	# 			tweet = json.loads(json.dumps(tweetin._json))
	# 			ret={}
	# 			try:
	# 				if not tweet["text"].find("RT"):
	# 					continue
	# 				ret["tweet_url"]=tweet["entities"]["urls"][0]["url"]
	# 				ret["expanded_url"]=tweet["entities"]["urls"][0]["expanded_url"]
	# 				hashtags=[]
	# 				for hashtag in tweet["entities"]["hashtags"]:
	# 					hashtags.append(hashtag["text"])
	# 				ret['hashtags']=hashtags
	# 				ret["created_at"]=tweet["created_at"]
	# 				ret["text"]=tweet["text"]
	# 				ret["lang"]=tweet["lang"]
	# 			except Exception, e:
	# 				pass
	# 			else:
	# 				print byteify(json.dumps(ret))
	querys = ['ESPN','USL','UCL','Arsenal','Luke Shaw', 'LFC']
	lang="ru"
	max_tweets = 5
	for query in querys:
		searched_tweets = [status for status in tweepy.Cursor(api.search, q=query,lang=lang).items(max_tweets)]
		for tweetin in set(searched_tweets):
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
				ret["text"]=tweet["text"]
				ret["lang"]=tweet["lang"]
			except Exception, e:
				pass
			else:
				with codecs.open("tweets2.json", "w", "utf-8") as stream:
					stream.write(byteify(json.dumps(ret)))

gettweets()