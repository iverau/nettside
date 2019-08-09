# Python OOP

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return self.first + " " + self.last

    def __str__(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)




em1 = Employee("Iver", "Ugelvik", 60000)

print(Employee.fullname(em1))

print(em1.__dict__)