from pydantic import BaseModel
from typing import Optional


class Consumer(BaseModel):
    '''Class for Consumer details.'''
    id: Optional[str]
    name: str
    image: Optional[str]
    block: str
    district: str
    sub_city: str
    house_number: int
    phone_number: str
    family_size: int
    token: Optional[str]
