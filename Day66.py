# Instance Variables and Class Variables in Python

'''
Class variables are the variables that are associated with a particular class and not its instances/objects
while, An Object variable is associated with an Object of a class and changes as per each Instance
'''

class employee:
    company = "Apple"
    employees = 0

    def __init__(self, name):
        self.name = name
        self.raiseAmt = 0.2
        employee.employees += 1

    def show(self):
        print(f"Employee name is {self.name} and is working in company {self.company} which has {self.employees} no of employees which have annual increment of {self.raiseAmt}%")



emp = employee("Yash")
emp.show()
emp.raiseAmt = 20
emp.company = "Netflix"
emp.show()

emp2 = employee("swami")
emp2.show()
emp2.company = "Google"
employee.show(emp2)

print(employee.company)
# here even though we have changed company name for both the employees
# still the main class variable has its original value
# ie. the variables is associated to the class