#!/usr/bin/python3
"""
This package initializes upon import, populating all objects in its instance private attribute __objects.
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

