#!/usr/bin/env python3
"""This module contains the base class for the AirBnB project
"""
from datetime import datetime
import time
import uuid


class BaseModel:
    """Defines all common attributes and methods for other classes
    """
    def __init__(self):
        """Class constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def save(self):
        """Updates the public instance attribute 'updated_at' 
           with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """_summary_
        """
        self.updated_at = self.updated_at.isoformat()
        self.created_at = self.created_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__

    def __str__(self):
        """Prints: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
