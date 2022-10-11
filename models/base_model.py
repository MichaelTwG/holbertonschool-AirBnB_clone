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
            cretaed_at - assign the datetime when the current instance is created
            updated_at - datetime when an istance is createad an when is updated
            
        __str__: print [<class name>] (<self.id>) <self.__dict__>
        
        Public Instance Methods:
            save(self): updates the public instance attribute updated_at 
                        with the current datetime
            to_dict(self): reeturns a dictionary containing all keys/values 
                           of the instance __dict__
            __dict__: a key must be added with the name of the object <__class__>
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
