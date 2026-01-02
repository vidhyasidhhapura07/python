# Create a Tuple with Duplicates

fruit = ("mango", "guava", "apple", "melon", "cheery", "grapes", "apple", "mango",)
print(fruit)

# Tuple Length

fruit = ("mango", "guava", "apple", "melon", "cheery", "grapes", "apple", "mango",)
print(len(fruit))

# tuple with data type

fruit = ("mango", "guava", "apple", "melon", "cheery" ,)
num = (1,2,3,4,5,6,7,8)
mix = (True, False, True, False)

print(type(fruit))
print(type(num))
print(type(mix))


# The tuple() Constructor

fruit = tuple(("mango", "guava", "apple", "melon", "cheery" ,))

print(fruit)

# index in tupal

fruit = ("mango", "guava", "apple", "melon", "cheery" ,)

print(fruit[2])
print(fruit[-2])  # negative index

# Range of Indexes in tupal

fruit = ("mango", "guava", "apple", "melon", "cheery", "grapes", "apple", "mango",)

print(fruit[1:3])
print(fruit[-4:-1]) # negative range
print(fruit[-5:-4]) # nagative range

# condition in tupal

fruit = ("mango", "guava", "apple", "melon", "cheery" ,)
if "guava" in fruit:
    print("Yes, 'guava' is in the fruits tuple")
else:
    print("No,  'guava' is in the fruits tuple ")


