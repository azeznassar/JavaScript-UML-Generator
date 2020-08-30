
from pickle import dump, load
from shelve import open as o
from os import remove, path


class Serializer():
    def __init__(self):
        self.serialized_data = "serialized.p"

    def serialize_a(self, data):
        if path.isfile(self.serialized_data):
            remove(self.serialized_data)
        with o(self.serialized_data, 'c') as shelf:
            shelf["js_class_data"] = data

    def serialize_b(self, data):
        with open(self.serialized_data, 'wb') as pfile:
            dump(data, pfile)

    def deserializer_a(self, args):
        try:
            with o(self.serialized_data, 'r') as shelf:
                for key in shelf.keys():
                    print(repr(key), repr(shelf[key]))
            if "-d" in args:
                remove(f'{self.serialized_data}.bak')
                remove(f'{self.serialized_data}.dat')
                remove(f'{self.serialized_data}.dir')

        except FileNotFoundError as file_not_found:
            print("""Make a UML diagram using the create_uml command 
            and then use deserialize. Error Message: """ + str(file_not_found))
        except:
            print("""Use create_uml first. DB shelve error. 
            Error message: dbm.error: db file doesn't exist;
            use 'c' or 'n' flag to create a new db""")

    def deserializer_b(self, args):
        try:
            with open(self.serialized_data, 'rb') as pfile:
                print(load(pfile))

            if "-d" in args:
                remove(self.serialized_data)

        except FileNotFoundError as file_not_found:
            print(f"""Generate a diagram using create_uml
                before using deserialize. Error Message:  {file_not_found}""")
