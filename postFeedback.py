from flask import Flask, request
import tweeter
import requests

app = Flask(__name__)

@app.route("/feedback", methods = ['POST'])
def feedback():
	feedback = request.get_json()
	return tweeter.tweet(feedback)
