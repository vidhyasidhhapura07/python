# Swap two variables using tuple unpacking.

n = 20
v = 10

print ("before swapping")
print("n = ",n)
print("v = ",v)

n , v = v , n

print("after swapping")

print("n = ",n)
print("v = ",v)


#  unpacking tupal

name = ("sachin", "niket", "yash", "dhurv", "kruparth")
(red , yellow, white, blue , green) = name


print(green)
print(blue)
print(red)
print(white)
print(yellow)

#  Using Asterisk*

name = ("sachin", "niket", "yash", "dhurv", "kruparth")
(red , yellow, *white) = name

print(red)
print(yellow)
print(white)
