from typing import Any, Optional
from pydantic import BaseModel, validator


class Image(BaseModel):
    '''Class for Image details.'''
    id: Optional[str]
    content: Any

    @validator("content")
    def validate_content(cls, val):
        if issubclass(type(val), bytes):
            return val

        raise TypeError(
            "subclass of bytes expected (type=type_error.subclass; expected_class=bytes)")
