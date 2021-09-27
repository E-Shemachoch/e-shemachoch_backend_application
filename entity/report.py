from pydantic import BaseModel
from typing import List, Optional


class Report(BaseModel):
    '''Class for Report details.'''
    income: float
    sold: int
    available: int
    date: int
