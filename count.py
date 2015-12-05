import codecs
import json
#2015-09-19 23:59:07+00:00
# Fri Sep 18 18:05:55 +0000 2015
import random
from pytz import timezone
from datetime import datetime
# docs=['tweets1','tweets2','tweets3','tweets4','tweets5']
count_dic={'ru':0,'de':0,'en':0}

a=100000000000000000
b=999999999999999999

# for doc in docs:2015
with codecs.open("all_tweet.json", "r") as stream:
	data=stream.read()
	jdata=json.loads(data)
	for tweet in jdata:
		fmt = '%Y-%m-%dT%H:%M:%SZ'
		temp = datetime.strptime(str(tweet['created_at ']),"%Y-%m-%d %H:%M:%S")
		tweet['created_at'] = str(temp.strftime(fmt))
		lang=tweet['lang']
		count_dic[lang]+=1
		with codecs.open("all_tweetc.json", "a") as stream:
			stream.write(str(json.dumps(tweet,ensure_ascii=False))+',\n')

print(count_dic)
