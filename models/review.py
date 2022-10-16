#!/usr/bin/python3
"""
    module state
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ classe review"""
    place_id = ""
    user_id = ""
    text = ""
