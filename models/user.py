#!/usr/bin/python3
'''User Class Module'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Initiallize User Class with public class attributes'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
