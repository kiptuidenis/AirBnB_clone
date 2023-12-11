#!/usr/bin/python3
"""
Module defines Unit tests for user.py
"""
import unittest
from models.user import User


class UserCase(unittest.TestCase):
    """Tests all instances and methods of User class"""
    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Bar"
    my_user.email = "airbnb@mail.com"
    my_user.password = "root"

    def test_user_init(self):
        "test if instance belongs to class"
        self.assertEqual(str(type(self.my_user)), "<class 'models.user.User'>")

    def test_attributes(self):
        "test attributes of class instance"
        self.assertEqual(self.my_user.first_name, "Betty")
        self.assertTrue(hasattr(self.my_user, 'email'))
        self.assertTrue(hasattr(self.my_user, 'password'))
        self.assertTrue(hasattr(self.my_user, 'last_name'))


if __name__ == '__main__':
    unittest.main()
