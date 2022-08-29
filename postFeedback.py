from flask import Flask, request, Response
import tweeter
import requests

app = Flask(__name__)

@app.route("/feedback", methods = ['POST'])
def feedback():
	feedback = request.get_json()
	result = {}

	# validate request for required fields
	if 'like' not in feedback:
		return Response("required field 'like' not present", status=400)

	tweeter.tweet(feedback)

	return Response("Thanks for the feedback!", 200)
