#!/usr/bin/python3

"""This module contains a class defintion of the Base models class"""

import uuid
import datetime
from models import storage


class BaseModel:
    """This class is the base class and it defines all
            common attributes/methods for other classes

            Attrbutes:
            id: string - assign with an uuid when an instance is created
            created_at: datetime - assign with the current datetime
                        when an instance is created
            updated_at: datetime - assign with the current datetime when an
                        instance is created and it will be updated every time
                        you change your object
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                elif 'created_at' in kwargs:
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif 'updated_at' in kwargs:
                    self.updated_at = datetime.datetime.fromisoformat(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()

        return object_dict
