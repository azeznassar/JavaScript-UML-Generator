import pickle
import shelve
from os import remove

class Serializer():
    def __init__(self):
        self.serialized_data = "serialized.p"

    def serialize_a(self, data):
        with shelve.open(self.serialized_data, 'c') as shelf:
            shelf["js_class_data"] = data

    def serialize_b(self, data):
        with open(self.serialized_data, 'wb') as pfile:
            pickle.dump(data, pfile)

    def deserializer_a(self, args):
        with shelve.open(self.serialized_data, 'r') as shelf:
            for key in shelf.keys():
                print(repr(key), repr(shelf[key]))
        if "-d" in args:
            remove(f'{self.serialized_data}.bak')
            remove(f'{self.serialized_data}.dat')
            remove(f'{self.serialized_data}.dir')

    def deserializer_b(self, args):
        with open(self.serialized_data, 'rb') as pfile:
            print(pickle.load(pfile))

        if "-d" in args:
            remove(self.serialized_data)