import tweepy
import config
import json

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, str):
        return input.decode('unicode_escape').encode('ascii','ignore')
    else:
        return input

def gettweets():
	auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
	auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	query = 'USOpen'
	lang="en"
	max_tweets = 20

	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query,lang=lang).items(max_tweets)]
	for tweetin in searched_tweets[1:]:
		tweet = json.loads(json.dumps(tweetin._json))
		ret={}
		try:
			ret["tweet_url"]=tweet["entities"]["urls"][0]["url"]
			ret["expanded_url"]=tweet["entities"]["urls"][0]["expanded_url"]
			ret["hashtags"]=tweet["entities"]["hashtags"][0]["text"]
			ret["created_at"]=tweet["created_at"]
			ret["text"]=tweet["text"]
			ret["lang"]=tweet["lang"]
		except Exception, e:
			pass
		else:
			print byteify(json.dumps(ret))


gettweets()