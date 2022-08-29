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
	author = feedback['author']
	like = feedback['like']
	comments = feedback['comments']

	tweet = author + ' ' + ('dis' if not like else '') + 'liked the Googli'

	if (comments):
		tweet = tweet + '\n\n' + comments

	tweet = tweet + '\n\n' + str(int(time.time()/100))
	return twitter.statuses.update(status=tweet)
