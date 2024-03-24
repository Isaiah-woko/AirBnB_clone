#!/usr/bin/python3

"""This module contains the user class"""

from models.base_model import BaseModel


class State(BaseModel):

    """Class inherits from BaseModel

    Public Class Attributes:
        name (str) - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.

        Parameters:
        *args: Positional arguments passed to the superclass constructor.
        **kwargs: Keyword arguments passed to the superclass constructor.
        """
        super().__init__(*args, **kwargs)
