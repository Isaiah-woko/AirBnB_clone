#!/usr/bin/python3

"""This module contains the user class"""

from models.base_model import BaseModel


class City(BaseModel):

    """Represents a user with email, password, first name, and last name."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.

        Parameters:
        *args: Positional arguments passed to the superclass constructor.
        **kwargs: Keyword arguments passed to the superclass constructor.
        """
        super().__init__(*args, **kwargs)
