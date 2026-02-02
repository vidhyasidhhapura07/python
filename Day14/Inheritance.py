# # Create a Parent Class

# class Full_Name:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# n = Full_Name("Niket Rajeshkumar","Dodiya")
# n.printname()

# # Create a child Class

# class animal:
#     def __init__(self,name):
#         self.name = name

#     def info(self):
#         print(f"Animal name: {self.name}")

# class Dog(animal):
#     def sound(self):
#         print(self.name, "barks")

# d = Dog("TOMMY")
# d.info()
# d.sound()


# # how to Use the super() Function with Add Properties


# class person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def Full_Name(self):
#         print(self.firstname, self.lastname)

# class Name(person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         self.year = "i am 25 year old"

# name = Name("Niket Rajeshbhai", "Dodiya")
# name.Full_Name()
# print(name.year)