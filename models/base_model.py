#!/usr/bin/python3
import uuid
import models
from datetime import datetime
"""This module contains a base class intended to be subclassed by many others
"""


class BaseModel:
    """Defines methods necessary for serialization and deserialization
    """
    def __init__(self, *args, **kwargs):
        """ Initialization
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Custom implementation of the __str__ method
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Saves changes made to the object
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary representation of an instance
        """
        dict_kv = {}
        dict_kv['__class__'] = self.__class__.__name__
        dict_kv['created_at'] = self.created_at.isoformat("T", "microseconds")
        dict_kv['updated_at'] = self.updated_at.isoformat("T", "microseconds")
        for key, value in self.__dict__.items():
            if key not in dict_kv.keys():
                dict_kv[key] = value
        return dict_kv

