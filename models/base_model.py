#!/usr/bin/python3

"""This module contains a class defintion of the Base models class"""

import uuid
import datetime
import models


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
        """Instance initialization function for every object

                Attributes:
                    id: unique ID
                    created_at: time created
                    updated_at: time updated

                Args:
                        id (str): uuid from dictionary
                        created_at (datetime): creation date and time
                        updated_at (datetime): updated date and time
                """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = str(value)
                elif key == 'created_at' and value is not None:
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif key == 'updated_at' and value is not None:
                    self.updated_at = datetime.datetime.fromisoformat(value)
                else:
                    if key != '__class__':
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates the public instance attribute "updated_at"
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of instance"""
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()

        return object_dict

    def __str__(self):
        """Returns a string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
