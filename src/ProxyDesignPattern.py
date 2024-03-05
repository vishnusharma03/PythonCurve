from abc import ABCMeta, abstractclassmethod


class Iperson:
    """
    The Proxy Design Pattern proviedes a pplaceholder for another object to control access to it.
    Thus provides more protection over access to that object.
    """
    @abstractclassmethod
    def person_method(self):
        """Interface Method"""

class Person(Iperson):
    def person_method(self):
        print("I am the Person")

class ProxyPerson(Iperson):
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("This is a Proxy Pattern Implementation")
        self.person.person_method()


if __name__=="__main__":
    # Controlled access to object.
    p1 = ProxyPerson()
    p1.person_method()


    # Direct Access to object
    p2 = Person()
    p2.person_method()




