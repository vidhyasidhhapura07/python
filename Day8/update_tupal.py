# # Update Tuples # #

# append()

fruit = ("mango", "guava", "apple", "melon", "cheery" ,)
n = list(fruit)
n.append ("grapes")
fruit = tuple(n)

print(fruit)

# Add tuple to a tuple (Concatenation)

fruit = ("mango", "guava", "apple", "melon", "cheery" ,)
n = ("grapes",)

fruit += n

print(fruit)

# Remove Items in tupal

fruit = ("mango", "guava", "apple", "melon", "cheery" ,)

n = list(fruit)
n.remove("guava")
fruit = tuple(n)

print(fruit)
 
# Tuple count() Method

fruit = ("mango", "guava", "apple", "mango", "cheery", "grapes", "apple", "mango",)

n = fruit.count("mango")
print(n)


# Built-in Function in tupal

name = tuple('Niket')
print(name)

# Deleting a Tuple

# fruit = ("mango", "guava", "apple", "mango", "cheery", "grapes", "apple", "mango",)
# del fruit

# print(fruit)

#  nested tupal

fruit = ('mango', 'guava', 'apple', 'melon', 'cheery' ,)
vitamins = ('a,b,c,d')

tupal = (fruit , vitamins)
print(tupal)

# Multiply Tuples

fruit = ('mango', 'guava', 'apple', 'melon', 'cheery' ,)
n = 2 * fruit
print(n)

