import json
import urllib2

screen_name = 'arrowgunz'
url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + screen_name
 
data = json.load(urllib2.urlopen(url))
 
print len(data), "tweets"
 
for tweet in data:
    print tweet['text']