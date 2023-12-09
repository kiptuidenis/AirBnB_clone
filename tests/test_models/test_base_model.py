#!/usr/bin/env python3
import unittest
from datetime import datetime
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    def test_BaseModel_init(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertEqual(my_model.my_number, 89)

    def test_base_model_save(self):
        """Tests the save method on the base model class"""
        base_model = BaseModel()
        date_now = datetime.now()
        base_model.save()
        diff = base_model.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_BaseModel_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict["my_number"], 89)
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
    
    def test_BaseModel__str__(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
