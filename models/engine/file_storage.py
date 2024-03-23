#!/usr/bin/python3

"""This module contains the definition for the file Storage class"""

import json
import os
from models.base_model import BaseModel


_cls = {
    "BaseModel": BaseModel,
    # Add other class names and corresponding classes as needed
}


class FileStorage:
    """This class has attributes and methods that serializes
        instances to a JSON file and deserializes JSON file to instances:

        Attributes:
        file_path: the path to the json file
        objects:
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """It returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """This function serializes an object into
            a json file"""

        every_obj = {}

        for obj in FileStorage.__objects:
            every_obj[obj] = FileStorage.__objects[obj].to_dict()
            with open(FileStorage.__file_path, "w") as json_file:
                json.dump(every_obj, json_file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                obj = json.load(json_file)
                for key, val in obj.items():
                    cls_name = val["__class__"]
                    cls = _cls.get(cls_name)
                    if cls:
                        FileStorage.__objects[key] = cls(**val)
        else:
            return
