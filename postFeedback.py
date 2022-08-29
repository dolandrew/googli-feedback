from flask import Flask, request
from pydantic import BaseModel
from typing import Optional
import requests

app = Flask(__name__)

class Feedback(BaseModel):
	like: bool
	author: Optional[str]

@app.route("/feedback", methods = ['POST'])
def feedback():
	# return request.get_json()
	return requests.get("https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles").json()
