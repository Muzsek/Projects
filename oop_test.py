class MyClass:
    x = 5

ex = MyClass()

#print(ex.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person(name = "John", age = 36)

#print(f"Name: {p1.name}, Age: {p1.age}") # John 36

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person1(name = "John",age = 36) 

#print(p1) #<__main__.Person object at 0x000001F1E3526CF0>

class Person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} , {self.age}"
    
p2 = Person2(name = "John", age = 23)

print(p2)