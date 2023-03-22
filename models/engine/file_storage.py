#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an interface to store data in JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary with all objects in the storage."""
        if cls is None:
            return self.__objects

        objects = {}
        for key, value in self.__objects.items():
            if isinstance(value, cls):
                objects[key] = value
        return objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save the objects to the file."""
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            objects = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(objects, f)

    def reload(self):
        """Load the objects from the file."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                objects = json.load(f)
                for key, value in objects.items():
                    class_name = key.split(".")[0]
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj

    def delete(self, obj=None):
        """Delete an object from the storage."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del self.__objects[key]

