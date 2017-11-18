import json
import oauth2 as oauth
from pprint import pprint

CONSUMER_KEY =	'kyxHUyO0hSpQMPpff4bFQDbLf'
CONSUMER_SECRET = 'NogkfrFF2NEjjBaykxJLzbTqEE95zwFCBg0Kftac2AOCnLmLoY'

ACESS_TOKEN = '4697983824-HZU1WduddJiX7zkAwlSvy6WbwNWp5PXQGfYZJUN'
ACESS_TOKEN_SECRET = 'A1N2shKiKynXo0eHRazwJVbwBnSR60MTTCyicuLhIysbC'

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
acess_token = oauth.Token(key=ACESS_TOKEN, secret=ACESS_TOKEN_SECRET)
client = oauth.Client(consumer, acess_token)

timeline_endpoint = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=bkrunner&count=1'
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    pprint(tweet)
