# a program to create a text file and write some content to it.

# file = open("first.txt" , "x")

with open("first.txt", "w") as f:

    f.write("Hello world...!\n")
    f.write("Welcome to Python file handling\n")
    f.write("This is line three\n")
    f.write("This is line four\n")

print()
f.close()

f = open("first.txt", "a")
f.write("world...!")
print()
f.close()

# Read the content of a file and print it.

file = open("first.txt" , "r")
print(file.read())
file.close()

# Write a program to count the number of lines in a file.

with open ("first.txt" , "r") as f:
    lines = f.readlines()
    print(len(lines))

