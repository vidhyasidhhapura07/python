# # Create a method in a class:

# class person:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("my name is " + self.name)
    
# p1 = person("Niket")
# p1.info()

# # Methods with Parameters

# class Calculator:
#     def add (self, N, V):
#         return N + V
     
#     def multipal(self, N, V):
#         return N * V

# abc = Calculator()

# print(abc.add(9,7))
# print(abc.multipal(9,7))


# Methods Modifying Properties

class python:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Certificat(self):
        print(f"Congratulations...! Dear {self.name} Cheers to you for a job WELL DONE...!" )    

p1 = python ("Niket Rajeshkumar Dodiya" , 25)
p1.Certificat()

# Multiple Methods

class movie:
    def __init__(self , name):
        self.name = name
        self.movie = []

    