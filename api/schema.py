from typing import List
from pydantic import BaseModel

class ImageGenReq(BaseModel):
    prompt: List[str]
    num_inference_steps: int
    guidance: float
    seed_val: int

class GenResponse(BaseModel):
    img: str
    inf_time: float