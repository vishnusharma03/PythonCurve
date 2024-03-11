
class Person:
    """
    Python does allow operator overloading whereas Java does not
    """

    def __init__(self, name, age, points):
        self.name = name
        self.age = age
        self.points = points

    def __str__(self):
        return f"Name is {self.name} & Age is {self.age} & Points is {self.points}"

    def __add__(self, other):
        return Person(self.name + other.name, self.age + other.age, self.points +other.points)

    def __sub__(self, other):
        return Person(self.name - other.name, self.age - other.age, self.points - other.points)

class Worker(Person):
    def __init__(self, name, age, points, salary):
        super(Worker, self).__init__(name, age, points)
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    # Method Overriding
    def __str__(self):
        text = super(Worker, self).__str__()
        text += f" salary is {self.salary}"
        return text




if __name__=="__main__":

    # W1 = Worker("Sharma", 23, 45, "Unknown")
    # print(W1)

    P1 = Person("Vishnu ", 23, 45)
    P2 = Person("Sharma", 1, 2)

    P3 = P1 + P2
    # Subtracting incompatible string type will throw error.
    P4 = P1 - P2

    print(P3)


# Additional
# method() : this is calling a method
# method : this is referring to it
