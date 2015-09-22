import codecs
import json
# Fri Sep 18 18:05:55 +0000 2015

from datetime import datetime
# docs=['tweets1','tweets2','tweets3','tweets4','tweets5']
count_dic={'ru':0,'de':0,'en':0}

# for doc in docs:
with codecs.open("alltweets.json", "r") as stream:
	data=stream.read()
	jdata=json.loads(data)
	for tweet in jdata:
		fmt = '%Y-%m-%dT%H:%M:%SZ'
		temp = datetime.strptime(str(tweet['created_at']),'%a %b %d %H:%M:%S %z %Y')
		tweet['created_at'] = str(temp.strftime(fmt))
		lang=tweet['lang']
		count_dic[lang]+=1
		with codecs.open("alltweets_c.json", "a") as stream:
			stream.write(str(json.dumps(tweet,ensure_ascii=False))+',\n')

print(count_dic)