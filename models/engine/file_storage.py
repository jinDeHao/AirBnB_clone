#!/usr/bin/python3
import json
from models import base_model


class FileStorage:

    __file_path = "save.json"
    __objects = {}

    def all(self):

        return self.__objects

    def new(self, obj):
        id = obj.id
        classname = obj.__class__
        
    


    def save(self):

        dictionary = dict(FileStorage.__objects)
        for key, value in dictionary.items():
            dictionary[key] = value.to_dict()
        
    with open(FileStorage.__file_path, "w") as file:
        file.write(json.dumps(dictionary))

    def reload(self):
        
        try:
            with open(self.__file_path, "r") as file:
                dictionary = json.loads(file.read())
        except FileNotFoundError:
            pass
        
