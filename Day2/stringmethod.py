# capitalize() (make first letter capital)
text="hello"
a = text.capitalize() 
print(a)

# casefold()(make first letter in lower case)
text="Hello"
a=text.casefold()
print(a)

# center() (sentence take-up space of characters)
text="Hello world...!"
x=text.center(50)
print(x)

# upper() (make all characters are in upper case.)
text="hello world...!"
n=text.upper()
print(n)

# title() ( first character in every word is upper case)
n=text.title()
print(n)

# swapcase()(Make the lower case letters upper case and the upper case letters lower case)
text= "HEllo WoRlD"
n=text.swapcase()
print(n)

# lower() (make all characters are in lower case)
text= "HELLO WORLD"
n=text.lower()
print(n)

# isupper()(Check if all the characters in the text are in upper case)
text= "HELLO WORLD"
n=text.isupper()
print(n)

# islower()(Check if all the characters in the text are in lower case)

text="hello world...!"
n=text.islower()
print(n)

# count()(Return the number of times the value "apple" appears in the string)

a="I love apples, apple are my favorite fruit"
b=a.count("apple")
print(b)

#endswith()(the string ends with the specified value Returns true)

a="I love apples, apple are my favorite fruit"
b=a.endswith("t")
print(b) # true

b=a.endswith("s")
print(b) #flase

# find() (Searches the string for a specified value and returns the position)

a="I love apples, apple are my favorite fruit"
b=a.find("apple")
print(b)

# format_map() ()


# rindex() (finds the last occurrence of the specified value.)

a="I love apples, apple are my favorite fruit"
b=a.rindex("are")
print(b)

# strip() (Returns a trimmed version of the string)

name="     xyz      "
b= name.strip()
print("my name is ",b," i am 20 year old...")

# maketrans() (use like replace)

fruits = ["mango","banana","apple"]
p=str.maketrans("apple", "guava")
print(fruits.translate(p))


# format_map() (the specified values of a dictionary and insert them inside the string's placeholders.)

detiles = {"name" : "XYZ" , "age" : 20 , "hight" : 5.3}
text = "my name is {name} i am {age} year old my hight is {hight} inch...!"
print(text.format_map(detiles))