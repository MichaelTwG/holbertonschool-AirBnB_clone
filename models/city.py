#!/usr/bin/python3
"""
    City Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class city, that inheriths from BaseModel """
    state_id = ""
    name = ""
