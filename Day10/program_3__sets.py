# Write a program to find common elements in two lists using sets.

list1 = ["niket", "new"]
list2 = ["Kruparth", "new"]

set1 = set(list1)
set2 = set(list2)

d = set1.intersection(set2)

print(d)
