#!/usr/bin/python3
""" Base Model Class """
import json
import csv


class Base:
    """ Represent the base model. """

    """
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new Base. """

        """
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON serialization of a list of dicts. """

        """
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON serialization of a list of objects to a file. """

        """
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Return the deserialization of a JSON string. """

        """
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return a class instantied from a dictionary of attributes. """

        """
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if cls.__name__ == "Rectangle":
            new_inst = cls(1, 1)
        else:
            new_inst = cls(1)
            new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """Return list of classes instantiated from a file of JSON strings."""

        """
        Returns:
            List of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Write the CSV serialization of a list of objects to a file. """

        """
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                c_wr = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    c_wr.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Return a list of classes instantiated from a CSV file. """

        """
        Returns:
            List of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in dicts.items())
                              for dicts in list_dicts]
                return [cls.create(**dicts) for dicts in list_dicts]
        except IOError:
            return []
