from pydantic import BaseModel
from typing import List

class LandmarkInput(BaseModel):
    landmarks: List[float]
