#!/usr/bin/python3
"""A script that defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Representa city.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
