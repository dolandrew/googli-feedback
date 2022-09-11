from flask import Flask, request, Response
from flask_docs_api.api import Api
from flask_cors import CORS, cross_origin
import tweeter
import requests

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/feedback", methods = ['POST'])
@cross_origin()
def feedback():
	feedback = request.get_json()
	result = {}

	# validate request for required fields
	if 'like' not in feedback:
		return Response("required field 'like' not present", status=400)

	tweeter.tweet(feedback)

	return Response("Thanks for the feedback!", 200)
