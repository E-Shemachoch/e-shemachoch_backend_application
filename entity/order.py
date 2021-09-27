from entity.product import Product
from pydantic import BaseModel
from typing import List, Optional


class Order(BaseModel):
    '''Class for Order details.'''
    id: Optional[str]
    products: List[Product]
    total_price: float
    total_quantity: int 
    consumer_id: str
    phone_number: str
    claimed: bool
    date: int
