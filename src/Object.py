

class Object:

    # Class Variables
    amount = 0

    def __init__(self, Name, Branch):
        self.Name = Name
        self.Branch = Branch
        Object.amount += 1

    def __del__(self):
        Object.amount -= 1

    def print(self):
        print(f"Name is {self.Name}")
        print(f"Branch is {self.Branch}")

    def __str__(self):
        return f"Name is {self.Name} & Branch is {self.Branch}"


if __name__=="__main__":

    o1 = Object("Vishnu", "CSE")
    # o1.print()
    print(o1)
