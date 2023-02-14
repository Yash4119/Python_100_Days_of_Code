# Single Inheritance in Python

class Animal:
    def __init__(self,name, id) -> None:
        self.name = name
        self.id = id

    def __str__(self) -> str:
        return (f"Animal name is {self.name} and its ID is {self.id}");

class Cat(Animal):
    def __init__(self, name, id) -> None:
        super().__init__(name, id)

    def sound(self):
        print("Meow")


cat = Cat("kiti",23)
cat.sound()
print(cat)
