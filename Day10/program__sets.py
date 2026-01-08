# Write a program that removes duplicates from a list using sets.

student = {"Niket", "Kruparth", "Dhurv", "Jiyansh"}
boys = {"Niket", "Yash", "Sachin", "Niket"}

nv = student.symmetric_difference(boys)
print(nv)

