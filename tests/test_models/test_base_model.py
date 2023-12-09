#!/usr/bin/env python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json

class TestBaseModel(unittest.TestCase):
    def test_BaseModel_init(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertEqual(my_model.my_number, 89)

    def test_base_model_instance_save(self):
        """Tests that model save"""
        base_model = BaseModel()
        base_model.save()
        key = "{}.{}".format(type(base_model).__name__, base_model.id)
        obj = {key: base_model.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(obj)))
            f.seek(0)
            self.assertEqual(json.load(f), obj)