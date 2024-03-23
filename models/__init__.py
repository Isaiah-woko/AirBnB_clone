#!/usr/bin/python3

"""This mosule conatins the initialzation for the python models"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
