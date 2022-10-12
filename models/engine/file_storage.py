#!/usr/bin/python3
""" Module File_Storage """
from json import dump, load
from models.base_model import BaseModel

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
        return self.__objects

    def new(self, obj):
        """ set obj in __objects """

        obj_dict = obj.to_dict()
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj_dict

    def save(self):
         with open(FileStorage.__file_path, mode="w") as File:
            dump(self.__objects, File)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r", encoding='utf-8') as File:
                my_dict = load(File)
                for key, dic in my_dict.intems():
                    FileStorage.__objects[key] == BaseModel(**dic)
        except FileNotFoundError:
            pass
        