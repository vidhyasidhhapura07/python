#Removing Items with POP method

student = {
    "name" : "Niket",
    "age" : 25,
    "city" : "surat"
 }
student.pop("age")
print(student)

#Removing Items with (POPITEM) method (popitem is removes the last items)

student = {
    "name" : "Niket",
    "age" : 25,
    "city" : "surat"
 }
student.popitem()
print(student)

# delete Items with del method 

student = {
    "name" : "Niket",
    "age" : 25,
    "city" : "surat"
 }
del student["age"]
print(student)

# full dictionary  delete with del method

# student = {
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat"
#  }
# del student
# print(student)


#  Removing full dictionary with .clear() method with empty block

student = {
    "name" : "Niket",
    "age" : 25,
    "city" : "surat"
 }

student.clear()
print(student)

