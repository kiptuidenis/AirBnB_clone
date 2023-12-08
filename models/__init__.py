#!/usr/bin/env python3
"""Creates a unique FileStorage instance for this application
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
