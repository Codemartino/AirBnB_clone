#!/usr/bin/python3
"""
    _init_ modules
"""
from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .review import Review
from .city import City
from .amenity import Amenity
from .place import Place
from .state import State

storage = FileStorage()
storage.reload()
