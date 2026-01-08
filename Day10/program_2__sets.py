# Write a program to perform union and intersection operations on sets.

student = {"Niket", "Kruparth", "Dhurv", "Jiyansh"}
boys = {"Niket", "Yash", "Sachin", "Niket"}

print("student" , student)
print("boys" , boys)

nv = student | boys

print("Union of student and boys:", nv)

vn = student.intersection(boys)

print("Intersection of student and boys:" , vn)