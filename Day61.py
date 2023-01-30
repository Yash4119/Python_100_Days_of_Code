# Inheritance in Python

'''
=> Inheritance is the feature of object oriented programming in which data items and methoda of an class can be used by another class

                            PARENT CLASS
                                 |
                                 |
                             CHILD CLASS
                                 
Inheritance can be of different types :- 

1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchial Inheritance
5. Hybrid Inheritance
'''

class Employee:
    def __init__(self, name, eid):
        self.name = name
        self.eid = eid
        print("In the Employee Class")
    
    def display(self):
        print(f"My name is {self.name} and my EID is {self.eid}")


class Programmer(Employee):
    # Here we inherited the Employee class in the Programmer class
    def __init__(self,name,eid):
        self.name = name
        self.eid = eid
        print("In the Programmer class")

    def show(self):
        print(f"I am a programmer, my name is {self.name} and EID is {self.eid}")


emp = Employee("Yash",3)
programmer = Programmer("Teja",11)

emp.display()
programmer.display()  # here we used the inherited method
programmer.show()
