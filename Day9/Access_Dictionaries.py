# # Accessing Items

# student = {
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat",
#  }

# n = student["name"]

# print(n)

# # Get Keys

# student = {
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat",
#  }
 
# n = student.keys()

# print(n)

# student ["DOB"]= "09-may-2001"

# print(n)

# # Get Values

# student = {
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat",
#  }
 
# n = student.values()

# print(n)

# student ["DOB"]= "09-may-2001"

# print(n)

# # Get Items
# student ={
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat",
# }
 
# n = student.items()

# print(n)

# student ["city"] = "Rajkot"

# print(n)

# # Check if Key Exists

# student ={
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat",
# }

# if "dob" in student:
#     print("yes...............!")
# else:
#     print("no....!")

# #  Update Dictionary

# student = {
#     "name" : "Niket",
#     "city" : "surat",
#     "age" : 25
#  }
# student.update({"age": 29})
# print(student)

# # Change Values in Dictionary 

# student = {
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat",
#  }

# student["city"]= "ahemdabad"

# print(student)

# # adding values in Dictionary 

# student = {
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat"
#  }

# student["DOB"]= "09-may-2001"
# print(student)

# # fromkeys() Method

# student = {"name", "age", "city", "dob"}
# v = 0
# n= dict.fromkeys(student,v)

# print(n)

# get() Method

# student = {
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat"
#  }
# n = student.get("age")
# print(n)

# # values() Method

# student = {
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat"
#  }

# n = student.values()
# print(n)

# keys() Method

# student = {
#     "name" : "Niket",
#     "age" : 25,
#     "city" : "surat"
#  }

# n = student.keys()
# print(n)

# setdefault() Method

student = {
    "name" : "Niket",
    "age" : 25,
    "city" : "surat"
 }

n = student.setdefault("DOB" , "9th May 2001")
print(n)