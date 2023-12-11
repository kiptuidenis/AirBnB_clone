#!/usr/bin/python3
"""Module defines class for reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines Review class
    With Attributes:
    place_id: string - empty string or the Place id
    user_id: string - empty string or the User id
    text: string - might be empty string
    """
    place_id = ""
    user_id = ""
    text = ""
