import tweepy
import config

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = 'USOpen'
lang="en"
max_tweets = 200

searched_tweets = [status for status in tweepy.Cursor(api.search, q=query,lang=lang).items(max_tweets)]

for tweet in searched_tweets:
	print tweet.text.encode('utf-8').strip()