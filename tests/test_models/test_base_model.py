#!/usr/bin/env python3
"This module contains tests for BaseModel class"
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines tests for attributes and methods of the BaseModel class
    """
    def test_BaseModel_init(self):
        "Tests Init method of BaseModel"
        test_model = BaseModel()
        test_model.name = "My First Model"
        test_model.my_number = 89

        self.assertEqual(test_model.my_number, 89)

    def test_base_model_save(self):
        """Tests the save method on the base model class"""
        base_model = BaseModel()
        time_now = datetime.now()
        base_model.save()
        diff = base_model.updated_at - time_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_BaseModel_to_dict(self):
        "Tests the to_dict method of BaseModel"
        test_model = BaseModel()
        test_model.name = "My First Model"
        test_model.my_number = 89
        test_model_dict = test_model.to_dict()
        self.assertEqual(test_model_dict["my_number"], 89)
        self.assertEqual(test_model_dict["__class__"], "BaseModel")

    def test_BaseModel__str__(self):
        "Tests __str__ method of BaseModel"
        test_model = BaseModel()
        test_model.name = "My First Model"
        test_model.my_number = 89
