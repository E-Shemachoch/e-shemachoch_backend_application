from pydantic import BaseModel
from typing import Optional


class Notice(BaseModel):
    '''Class for Notice details.'''
    id: Optional[str]
    title: str
    message: str
    date: int
