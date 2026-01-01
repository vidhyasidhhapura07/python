# Using Square Brackets

number = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
name = ["sachin", "niket", "yash", "dhurv", "kruparth"]
mix = ["jiyansh", 5, 7.9, True]
print(number)
print(name)
print(mix)

# Creating List with Repeated Elements

a = [0] * 1
b = [1] * 2
c = [2] * 3
d = [3] * 4
print(a)
print(b)
print(c)
print(d)

# Updating Elements into List

name = ["sachin", "niket", "yash", "dhurv", "kruparth"]
number = [7, 14, 20, 28, 35, 42, 49, 56, 63, 70]

name[2]="jiyansh"
number[2] = 21

print(name)
print(number)

# Removing Elements from List


name = ["sachin", "niket", "yash", "dhurv", "kruparth"]
mix = ["jiyansh", 5, 7.9, True]

name.remove("yash")
mix.remove(5)

print(name)
print(mix)

# Iterating Over Lists (like a for loop)


name = ["Sachin", "Niket", "Yash", "Dhurv", "Kruparth"]
for n in name:
    print(n)

# Nested Lists

mix =[  ["Niket", "Yash", "Kirtan"],
        [2001, 2002, 2003],
        [6.3, 5.4, 9.5],
        [True, False]
    ]
print(mix[0][0])
print(mix[1][0])
print(mix[2][2])
print(mix[3][0])

