# Python File create

# n = open("abc.txt" , "x")

# Python File Open

n = open("abc.txt")

#Python Close Files

n = open("abc.txt" , "r")
print(n.readline())
n.close()

# Using the with statement

with open ("abc.txt") as f:
    print(f.read())

# Using the with statement to write

with open ("abc.txt", "w") as f:
    f.write("hello everyone...!")

with open("abc.txt") as f:
    print(f.read())

# Using the with statement to Append 

with open ("abc.txt" , "a") as f:
    f.write("this is my first txt program")

with open("abc.txt") as f:
    print(f.read())

# Delete a File

# import os
# os.remove("abc.txt")


