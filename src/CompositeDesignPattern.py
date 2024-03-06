from abc import abstractstaticmethod, ABCMeta, abstractmethod


class IDepartment:
    """
    Composite Design Pattern allows to create hierarchies between objects.
    Both leaf & composite objects are treated uniformly.
    It provides flexibility in using the objects.
    """

    @abstractmethod
    def __init__(self):
        """Will be implemented in child classes"""

    @abstractstaticmethod
    def print_data():
        """Again will be implemented in child classes."""


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_data(self):
        print(f"Accounting has {self.employees} employees.")


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_data(self):
        print(f"Development Department has {self.employees} employees.")


class VahanAuto(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_dept = []

    def __add__(self, sub_dept):
        self.sub_dept.append(sub_dept)
        self.employees += sub_dept.employees

    def print_data(self):
        print(f"Base Employees: {self.base_employees}")
        for dept in self.sub_dept:
            # print(f"Employeers in Department {dept} is {dept.employees}")
            dept.print_data()
        print(f"Total Employees : {self.employees}")


if __name__ == "__main__":
    D1 = Development(142)
    # D1.print_data()

    D2 = Accounting(90)
    # D2.print_data()

    PD = VahanAuto(30)
    PD.__add__(D1)
    PD.__add__(D2)
    PD.print_data()
