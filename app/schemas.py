from pydantic import BaseModel, validator
from typing import List

class LandmarkInput(BaseModel):
    landmarks: List[float]

    @validator('landmarks')
    def check_length(cls, v):
        expected_length = 63  
        if len(v) != expected_length:
            raise ValueError(f'landmarks must have exactly {expected_length} floats')
        return v
