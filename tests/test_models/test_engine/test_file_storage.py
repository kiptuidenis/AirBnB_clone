#!/usr/bin/python3
"""This module contains tests for the Filestorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Defines TestClass for attributes and methods of the FileStorage class
    """
    def test_FileStorage_init(self):
        """Tests initializtion of FileStorage class
        """
        test_storage = FileStorage()
        self.assertEqual(test_storage.__class__, FileStorage)
        test_storage = None

    def test_FileStorage_all(self):
        """Tests the all() method of FileStorage class
        """
        test_storage = FileStorage()
        self.assertIsNotNone(test_storage.all())
        self.assertDictContainsSubset({}, test_storage.all())
        test_storage = None

    def test_FileStorage_new(self):
        """Tests the new() method of FileStorage class
        """
        test_storage = FileStorage()
        count = len(test_storage.all())
        test_basemodel = BaseModel()
        test_basemodel.name = "My First Model"
        test_basemodel.my_number = 89
        test_storage.new(test_basemodel)
        self.assertEqual(len(test_storage.all()), count + 1)

    def test_FileStorage_reload(self):
        """Tests the reload() method of FileStorage class
        """
        test_storage = FileStorage()
        test_storage.reload()
        test_basemodel = BaseModel()
        test_basemodel.name = "My First Model"
        test_basemodel.my_number = 89
        test_storage.new(test_basemodel)
        initial = test_storage.all()
        test_storage.reload()
        self.assertNotEquals(initial, test_storage.all())
        self.assertEqual(len(initial), len(test_storage.all()) + 1)

    def test_FileStorage_save(self):
        """Tests the save() method of FileStorage class
        """
        test_storage = FileStorage()
        test_storage.reload()
        test_basemodel = BaseModel()
        test_basemodel.name = "My First Model"
        test_basemodel.my_number = 89
        test_storage.new(test_basemodel)
        test_storage.save()
        initial = test_storage.all()
        test_storage.reload()
        self.assertNotEquals(initial, test_storage.all())
        self.assertEqual(len(initial), len(test_storage.all()))
<<<<<<< HEAD

if __name__ == '__main__':
    unittest.main()
=======
    def test_instances(self):
        """Test for storage instance"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)
>>>>>>> cebe6a660e24f5be30d97895bcf6d9ef63bf877d
