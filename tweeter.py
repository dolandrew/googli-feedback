from feedback import Feedback
from twitter import *
import requests, time, os

twitter = Twitter(
	auth = OAuth(
		os.environ.get('OAUTH_TOKEN'),
		os.environ.get('OAUTH_SECRET'),
		os.environ.get('CONSUMER_KEY'),
		os.environ.get('CONSUMER_SECRET')
	)
)

def tweet(feedback: Feedback=None):
	like = feedback['like']

	if 'author' not in feedback:
		feedback['author'] = 'Someone'

	tweet = feedback['author'] + ' ' + ('dis' if not like else '') + 'liked the Googli'
	if 'comments' in feedback:
		tweet = tweet + '\n\n' + feedback['comments']

	tweet = tweet + '\n\n' + str(int(time.time()))
	return twitter.statuses.update(status=tweet)
