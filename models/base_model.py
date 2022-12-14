#!/usr/bin/python3
"""
    Module BaseModel - create a Base Class
    that defines all common attributes/methods for other classes
"""
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4
import models


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
    def __init__(self, *args, **kwargs):
        """ The constructor of the class """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs is not None:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                self.__dict__[key] = val
        models.storage.new(self)

    def __str__(self):
        """ format when the object is printed """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ actually only update the date when the instance is saved """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            convert the class in a dictionary,
            and the key with the name of the class
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
