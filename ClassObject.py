#Creating Class

class Student:
    name = "John"

#Creating Object (Instance)
S1 = Student()
print(S1.name)

# __init__() function : Constructor

class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        print("Welcome", self.name)

# Creating Object (Instance)
S1 = Students("John", 20)
S1.welcome()
print(S1.name, S1.age)

S2 = Students("Alice", 22)
S2.welcome()
print(S2.name, S2.age)