from pydantic import BaseModel
from typing import Optional

class Feedback(BaseModel):
	like: bool
	author: Optional[str]
