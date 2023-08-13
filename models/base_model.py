#!/usr/bin/python3
"""
Provides a class 'BaseModel' to serve as a base class for all other models
"""
import models
from datetime import datetime
from uuid import uuid4


ISOFORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Defines functionality common to all models
    """

    def _init_(self, *args, **kwargs):
        """
        Instantiate a model
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, ISOFORMAT))
                elif key != "_class_":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def _str_(self):
        """
        Convert a model to a string
        """
        return "[{model}] ({ident}) {attrs}".format(
            model=self._class.name_,
            attrs=self._dict_,
            ident=self.id,
        )

    def save(self):
        """
        Save a model to the filesystem
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert a model to a dictionary
        """
        dictionary = self._dict_.copy()
        dictionary["_class"] = self.class.name_
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["created_at"] = self.created_at.isoformat()
        return dictionary
