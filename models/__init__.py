#!/usr/bin/python3

"""This module contains the initialization for the python models"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
