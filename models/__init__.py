#!/usr/bin/python3
from models.engine.file_storage import FileStorage


"""Set modules for import"""
__all__ = ["base_model"]

"""Unique storage object"""
storage = FileStorage()

"""Reload all the objects saved in the JSON file"""
storage.reload()
