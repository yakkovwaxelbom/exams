from pydantic import BaseModel
from typing import Literal


class RequestsCaesar(BaseModel):
    text: str
    offset: int
    mode: Literal['encrypt', 'decrypt']


class RequestsFence(BaseModel):
    text: str
