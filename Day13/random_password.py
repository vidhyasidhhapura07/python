# Write a program to generate a random password using the string and random modules.

import random
import string


# Upper letter
first = random.choice(string.ascii_uppercase)

# Lowwer letter (4)
second = ''.join(random.choices(string.ascii_lowercase, k=4))

# Special character
special = random.choice(string.punctuation)

# digits
last = ''.join(random.choices(string.digits, k=3))

password = first + second + special + last

print("your strong password is: " ,password)


# Write a program to generate a random password using the string and random modules with username with all password condition


# import random
# import string

# name = input("enter user name: ")

# # upper case
# first = random.choice(string.ascii_uppercase)

# # lowwercase
# second = ''.join(random.choices(string.ascii_lowercase, k=2))

# # special
# special = random.choice(string.punctuation)

# # digit
# last = ''.join(random.choices(string.digits, k=4))

# password = first + second + special + last

# final_password = name + '.' + password

# print ("your strong password is: " , final_password)