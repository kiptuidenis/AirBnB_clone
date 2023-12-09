#!/usr/bin/python3
"""Tests file_storage"""
import unittest
from models.engine.file_storage import FileStorage

class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""
    def test_instances(self):
        """Test for storage instance"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)