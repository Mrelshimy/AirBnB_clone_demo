#!/usr/bin/python3
""" State Class Module"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    The State class inherits from the BaseModel class.
    It represents a state with attributes for
    name.

    Attributes:
        name (str): The name of the state.
    """

    name = ""

    def __init__(self):
        """
        Constructor for the State class.

        Parameters:
            name (str, optional): The name of the state. Defaults to "".
        """
        pass
