#!/usr/bin/python3
""" base model"""

import json


class Base:
    """ Base claas which serve as parent class for other classes"""
    __nb_object = 0

    """Base class Constructor"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method: to_json_string
        Args:
            1. list_dictionaries - is a list of dictionaries
        Return: Returns the JSON string representation of list_dictionaries
        or "[]" if list_dictionariers is empty
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method: save_to_file
        Args:
            1. list_obj - is a list of instances who inherits of Base.
        Use: write json representation of objects to a file
        Return: Nothing
        """

        obj_class = cls.__name__
        file_ext = ".json"
        file_name = obj_class + file_ext
        if list_objs is not None:
            objects = []
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                objects.append(obj_dict)
        else:
            objects = list()
        with open(file_name, "w", encoding='utf-8') as f:
            f.write(cls.to_json_string(objects))

    @staticmethod
    def from_json_string(json_string):
        """
        Method: from_json_string
        Args:
            1. json_string - string representing a list of dictionaries
        Return: list of the JSON string representation json_string
        """

        if json_string is None or json_string == "":
            obj_list = []
            return obj_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Method: create()
        Args:
            1. dictionary - double pointer to a dictionary
        Return: instance with all attribute set
        """

        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Method: load_from_file()
        Return: return list of instance
        """

        try:
            with open(f"{cls.__name__}.json", 'r') as f:
                data = json.load(f)
                instances = [cls(**instance) for instance in data]
                return instances
        except FileNotFoundError:
            return []
