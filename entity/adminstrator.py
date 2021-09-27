from pydantic import BaseModel
from typing import Optional


class Adminstrator(BaseModel):
    '''Class for Adminstrator details.'''
    id: Optional[str]
    username: str
    password: str
    token: Optional[str]
