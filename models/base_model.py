#!/usr/bin/python3
"""
    Module BaseModel - create a Base Class
    that defines all common attributes/methods for other classes
"""
from datetime import datetime
from uuid import uuid4
import time


class BaseModel:
    """
        BaseModel - the BaseClass

        Public Attribs:
            id - idintificate an istance of the object - generated by UUID
            cretaed_at - assign datetime when the an instance is created
            updated_at - assign datetime when an istance is createad or updated

        __str__: print [<class name>] (<self.id>) <self.__dict__>

        Public Instance Methods:
            save(self): updates the public instance attribute updated_at
                        with the current datetime
            to_dict(self): reeturns a dictionary containing all keys/values
                           of the instance __dict__
            __dict__: added a key <__class__> with name of the class
    """
    def __init__(self):
        """ The constructor of the class """
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def __str__(self):
        """ format when the object is printed """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ actually only update the date when the instance is saved """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """
            convert the class in a dictionary,
            and the key with the name of the class
        """
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
