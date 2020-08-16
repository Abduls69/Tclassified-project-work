#  A class is a blueprint for creating objects. An object has properties and methos(functions) associated with
# ALmost everything in python is an object that is why python is an object oriented programming language- OOP

# Create class

class Students:
    # constructor 
    def __init__(self, name, email, age):
        self.name = name 
        self.email = email
        self.age = age
       
    def greeting(self):
        return f'I am a student with name {self.name} and i am {self.age}'

    def has_birthday(self):
        self.age +=1

# Create an object of class students
fortune = Students('onyekwere fortune', 'onyekwerefortune1@gmail.com', 21)

# Extend class (inheritance)

class StudentRep(Students):
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age 
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'I am the class rep with name {self.name} and i am {self.age} and my balance is {self.balance}'

# Create an object of class students
fortune = Students('Onyekwere Fortune', 'onyekerefortune@gmail.com', 21)

# Create and Object of class StudentRep
joshua = StudentRep('Ndubueze Joshua', 'josheze58@gmail.com', 20)

joshua.set_balance(800)
print(joshua.greeting())

    