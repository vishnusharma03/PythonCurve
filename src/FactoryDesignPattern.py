# Imports for abstract classes & methods
from abc import ABCMeta, abstractclassmethod




class Iperson(metaclass=ABCMeta):
    """
    The idea of Factory design pattern is to create objects without specifying the exact class
    of which the object will be created.
    This is decided at runtime.
    Helps to decouple the creation of objects with their implementation
    """

    @abstractclassmethod
    def person_method(cls):
        """Instance Method"""
        print("Sharma")  # I am not sure why I am allowed to pass this here.


class Student(Iperson):

    def __init__(self):
        self.name = "Vishnu Sharma"

    def person_method(cls):
        print("SV stands for Special Vehicle.")


class Teacher(Iperson):

    def __init__(self):
        self.name = "Vishal Sharma"

    def person_method(cls):
        print("SV is my favourite")


class PersonFactory:

    @staticmethod
    def buildPerson(designation : str):
        if designation=="Student":
            return Student()
        if designation=="Teacher":
            return Teacher()
        print("Invalid type")
        return -1 # Or additionally throw an exception

    # Here I could have defined a sophisticated Non-static method to decide which type of object
    # I want to create at runtime.


if __name__ == "__main__":
    # s1 = Student()
    # s1.person_method()
    choice = input("Enter Designation: ")
    person = PersonFactory.buildPerson(choice)
    person.person_method()



# LearningIteration101

# This I here in "Iperson" is sort of convention to define interfaces.
# class Iperson(metaclass=ABCMeta):
#
#     @abstractclassmethod
#     def person_method(cls):
#         """Instance Method"""
#         print("Sharma")
#
# class Student(Iperson):
#
#     def __init__(self):
#         self.name = "Vishnu Sharma"
#
#
# if __name__=="__main__":
#     ## Abstract classes defined cannot have instances of it,
#     ## so below code yields error.
#     # p1 = Iperson()
#     # p1.person_method()
#
#
#     ## TypeError: Can't instantiate abstract class Student without an implementation for abstract method 'person_method'
#     # p2 = Student()
#
