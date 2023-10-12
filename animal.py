class Animal:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)
    
    def hasBirthday(self):
        self.age = self.age +1

class Cat(Animal):
    def getSound(self):
        print("miau")

class Dog(Animal):
    def getSound(self):
        print("wuw")