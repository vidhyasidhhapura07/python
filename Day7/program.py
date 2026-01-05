# Create and manipulate a list of numbers or strings.
    
    # append


number = [7, 14, 21, 28, 35]
name = ["sachin", "niket", "yash", "dhurv", "kruparth"]

number.append(42)
name.append("jiyansh")
print(number)
print(name)

    # copy 

number = [7, 14, 21, 28, 35]
name = ["sachin", "niket", "yash", "dhurv", "kruparth"]

n = number.copy()
d = name.copy()
print(n)
print(d)

    # clear():

number = [7, 14, 21, 28, 35]
name =  ["sachin", "niket", "yash", "dhurv", "kruparth"]

number.clear()
name.clear()

print(number)
print(name)

    # count():

number = [7, 14, 21, 28, 35,14,65,15,14]
name =  ["sachin", "niket", "yash", "dhurv", "niket", "kruparth"]

print(number.count(14))
print(name.count("niket"))

    # extend():

number = [7, 14, 21, 28, 35]
name =  ["sachin", "niket", "yash", "dhurv", "kruparth"]

number.extend([42, 49, 56, 63, 70])
name.extend(["jiyansh"])

print(number)
print(name)

    # index():

number = [7, 14, 21, 28, 35]
name =  ["sachin", "niket", "yash", "dhurv", "kruparth"]

print(number.index(21))
print(name.index("niket"))


    # insert():

number = [7, 14,  28, 35]
name =  ["sachin", "yash", "dhurv", "kruparth"]

number.insert(2, 21)
name.insert(1,"niket")

print(number)
print(name)

    # pop():

number = [7, 14,  28, 35]
name =  ["sachin", "niket", "yash", "dhurv", "kruparth"]
number.pop()
name.pop()

print(number)
print(name)

    # remove():

number = [7, 14, 21, 28, 35]
name =  ["sachin", "niket", "yash", "dhurv", "kruparth"]

number.remove(21)
name.remove("yash")

print(number)
print(name)

    # reverse():

number = [7, 14, 21, 28, 35]
name =  ["sachin", "niket", "yash", "dhurv", "kruparth"]

number.reverse()
name.reverse()

print(number)
print(name)

    # sort():

number = [7, 14, 21, 28, 35]
name =  ["sachin", "niket", "yash", "dhurv", "kruparth"]

number.sort()
name.sort()

print(number)
print(name)
