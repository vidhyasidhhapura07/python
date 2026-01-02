# simple for loop in tupal

fruit = ('mango', 'guava', 'apple', 'melon', 'cheery' ,)

for x in fruit:
    print(x)

# for loop with range() & len() function  {2nd way using for loop}

fruit = ('mango', 'guava', 'apple', 'melon', 'cheery' ,)

for n in range(len(fruit)):
    print(fruit[n])

# While Loop in tupal

fruit = ('mango', 'guava', 'apple', 'melon', 'cheery' ,)
n = 0
while n > len(fruit):
    print(fruit[n])
    n = n + 1

# for loop with range() & len() function 

name = 'Niket'
v = 6
for v in range(int(v)):
    name = (name,)
    print(name)