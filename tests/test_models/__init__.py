#!/usr/bin/python3
"""
Upon import, this package initializes, populating all objects in its instance private attribute __objects
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

