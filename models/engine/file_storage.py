#!/usr/bin/python3
"""This module serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import datetime
import json
import os


class FileStorage:
    """serializes instances to a JSON file and
       deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objets the obj with key <obj class name>.id

        Args:
            obj (Object): Object to be stored
        """
        self.key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[self.key] = obj

    def save(self):
        """Save the __objects to JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            all_objects = {key: obj.to_dict() for key, obj in FileStorage.
                           __objects.items()}
            json.dump(all_objects, f)

    def reload(self):
        """Fetch the JSON file to __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {
                key: self.classes()[obj["__class__"]](**obj)
                for key, obj in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def classes(self):
        """Returns classes"""
        from models.base_model import BaseModel
        from models.user import User

        classes = {"BaseModel": BaseModel, "User": User}
        return classes

    def attributes(self):
        """Returns classname and the attributes"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime}
        }
        return attributes
