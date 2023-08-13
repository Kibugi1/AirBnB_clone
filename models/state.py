#!/usr/bin/python3
"""A script that defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.
    Attributes:
        name (str): The name of the state.
    """

    name = ""
