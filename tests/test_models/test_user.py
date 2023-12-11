#!/usr/bin/python3
"""
Module defines Unit tests for user.py
"""
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    """Tests all instances and methods of User class"""
    u = User()
    

if __name__ == '__main__':
    unittest.main()