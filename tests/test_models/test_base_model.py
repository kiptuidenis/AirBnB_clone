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
    def test_base_model_to_dict(self):
        """Tests for to_dict()  on the base model class"""
        base_model = BaseModel()
        base_model.name = "Gabriel"
        base_model.age = 30
        user = base_model.to_dict()
        self.assertEqual(user["id"], base_model.id)
        self.assertEqual(user["__class__"], type(base_model).__name__)
        self.assertEqual(user["created_at"], base_model.created_at.isoformat())
        self.assertEqual(user["updated_at"], base_model.updated_at.isoformat())
        self.assertEqual(user["name"], base_model.name)
        self.assertEqual(user["age"], base_model.age)
