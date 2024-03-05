from abc import ABCMeta, abstractstaticmethod



class IPerson(metaclass=ABCMeta):
    """
    The idea behind Singleton class that it can only be instantiated once.
    """
    @abstractstaticmethod
    def print_data():
        """Interface Method"""


class Person(IPerson):
    def __init__(self, name):
        self.name = name

    def print_data(self):
        print("Name: ", self.name)


class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("x", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton Class can't be initialized twice")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self


    def print_data(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")


if __name__ == "__main__":
    p1 = Person('Sharma2')
    p1.print_data()

    p2 = Person('Sharma3')
    p2.print_data()

    # Default
    p3 = PersonSingleton.get_instance()
    p3.print_data()

    # First Initiation
    p3 = PersonSingleton("Vishnu", 23)
    p3.print_data()

    # Second Initiation
    p4 = PersonSingleton("Prabhat", 24)
    p4.print_data()
