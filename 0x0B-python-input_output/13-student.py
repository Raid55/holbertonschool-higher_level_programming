#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and type(attrs) is list:
            return {key: value for key, value in self.__dict__.items() if key in attrs and type(key) is str}
        else:
            return self.__dict__
        
    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
