# Super keyword in Python

'''
Super keyword is basically used to refer the parent class
'''

class employee:
    def __init__(self, name , id) -> None:
        self.name = name
        self.id = id

    def show(self):
        print(f"Employee Id is { self.id } and Employee name is {self.name}")


class programmer(employee):
    def __init__(self, name, id, lang) -> None:
        super().__init__(name, id)
        self.lang = lang

    def show(self):
        print(f"Programmer name is {self.name} and Works on language {self.lang}")

    def __str__(self):
        return f"This is the Programmer class for instance {self.name}"

    def __call__(self, num):
        return self.id*num
    
    def __len__(self):
        return len(self.name)

    def __repr__(self) -> str:
        return f"This is the Programmer class for instance {self.name} repr."


p1 = employee("Yash",201)
p2 = programmer("Swami Ji",412, "Physics Wallah")

p1.show()
p2.show()
print(p2.name)