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
