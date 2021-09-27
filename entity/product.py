from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    '''Class for Product details.'''
    id: Optional[str]
    name: str
    price: float
    quantity: int
    initial_quantity: Optional[int]
    image: Optional[str]
    date: int
