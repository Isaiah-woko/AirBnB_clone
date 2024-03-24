#!/usr/bin/python3
"""This Module contains the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class inherits from BaseModel

    Public Class Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.

        Parameters:
        *args: Positional arguments passed to the superclass constructor.
        **kwargs: Keyword arguments passed to the superclass constructor.
        """
        super().__init__(*args, **kwargs)
