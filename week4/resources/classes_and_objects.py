"""
The simplest form of class definition has the following format:
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""

class Dog:
    def __init__(self, name, breed, age, color, size):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.size = size
    
    def bark(self):
        print("Woof...Woof")
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age

dog1 = Dog("Max","German Shepherd",2,"brown","large")
dog2 = Dog("Cooper","Labrador",4,"black","large")
dog3 = Dog("Bella","Chihuahua",1,"tan","small")   

print(dog1.getName())
dog1.bark()

dog2.setAge(5)
print(dog2.age)