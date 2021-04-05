# WRONG!!!
# class Animal:
#
#     def __init__(self, name):
#         self.__name = name
#
#     def get_animal_name(self):
#         return self.__name
#
#     def save_animal(self):
#         pass


class Animal:
    def __init__(self, name):
        self.__name = name

    def get_animal_name(self):
        return self.__name


class AnimalDB:

    def __init__(self, a):
        self.__animal = a

    def det_animal(a: Animal):
       return a

    def save_animal(self):
        pass