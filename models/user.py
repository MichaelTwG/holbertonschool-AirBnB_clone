#!/usr/bin/python3
""" Module user """

from lib2to3.pytree import Base
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
