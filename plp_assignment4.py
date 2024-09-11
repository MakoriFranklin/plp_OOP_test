class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f'Hello, my name is {self.name}. Am {self.age}. Am {self.gender}')
instance = Person(name="Franklin", age=20, gender="Male")
instance.introduce()