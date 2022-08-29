from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import requests

app = FastAPI();

class Feedback(BaseModel):
	like: bool
	author: Optional[str]

@app.post("/feedback")
def root(feedback: Feedback):
	return requests.get("https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles").json()
