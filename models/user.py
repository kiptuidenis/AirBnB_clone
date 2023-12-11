#!/usr/bin/python3
'''User Class Module'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Initialize User Class with public class attributes'''

    def __init__(self, *args, **kwargs):
        '''Initialize instance attributes'''
        super().__init__(*args, **kwargs)  # Call the __init__ method of the base class
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
