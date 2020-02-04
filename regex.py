import html
import unicodedata
import re


original_tweet = "I luv my &lt;3 iphone &amp; you’re awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com  &#62"

tweet=html.unescape(original_tweet)
#tweet1=html.escape(original_tweet)
print(original_tweet)
print(tweet)
#print(tweet1)
print(unicodedata.normalize('NFKD', tweet).encode('ascii','ignore'))
tweet=unicodedata.normalize('NFKD', tweet).encode('ascii','ignore')
re.sub(rb'http\S+', '', tweet)