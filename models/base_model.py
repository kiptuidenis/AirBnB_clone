#!/usr/bin/env python3
"""This module contains the base class for the AirBnB project
"""
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """Defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Class constructor
        """
        if len(kwargs) != 0:
            del kwargs['__class__']
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates the public instance attribute 'updated_at' 
           with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary with all keys/values of __dict__ of the instance
        """
        MyDict = self.__dict__.copy()
        MyDict["__class__"] = type(self).__name__
        MyDict["created_at"] = MyDict["created_at"].isoformat()
        MyDict["updated_at"] = MyDict["updated_at"].isoformat()
        return MyDict

    def __str__(self):
        """Prints: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
