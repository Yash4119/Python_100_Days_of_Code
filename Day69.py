# Class Methods in Python

'''
Classes are used to build custom data types
Class method is a type of method that is bound to the class and not to the instance of the class
'''

class employee:
    compName = "Apple"

    def __init__(self):
        print(f"This company name is {self.compName}")

    def show(self):
        print(f"{self.name} is an employee of {self.compName}")

    @classmethod
    def changeName(cls, newName):
        # Here whether we use cls or self both are the same
        cls.compName = newName


e1 = employee()
e1.name = "Yash"
e1.show()
e1.changeName("Google India")
e1.show()
# here the variable compName is bound to the instance and hence changename function dosent changes the original name of the variable. To avoid this use the decorator @ClassMethod to make is a class bound variable and this makes a class avalable for updation of its variables
print(employee.compName)
