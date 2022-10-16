#!/usr/bin/python3
""" Module File_Storage """
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
        Serializes and Deserializes instances to a JSON file
            Atribs:
                Privates:
                __file_path: path to the JSON file
                __objects: (empty dictionart)
                           but will store all objects
            Mhetods:
                all: return the dictionary __object
                new: sets in the with ey __objects obj
                save: serialize to the JSON file
                reload: deserializes the JSON
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return all"""
        return FileStorage.__objects

    def new(self, obj):
        """ set obj in __objects """
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj

    def save(self):
        save_dict = {}
        with open(self.__file_path, 'w') as File:
            for key, value in self.__objects.items():
                save_dict[key] = value.to_dict()
            json.dump(save_dict, File)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                Sdict = json.load(file)
                for val in Sdict.values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(class_name)(**val))

        except FileNotFoundError:
            pass
    
    def classes(self):
        dict_of_classes = {
            "BaseModel": BaseModel(),
            "User": User(),
            "Place": Place(),
            "State": State(),
            "City": City(),
            "Amenity": Amenity(),
            "Review": Review()}
        return dict_of_classes