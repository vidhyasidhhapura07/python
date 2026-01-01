# Recursion

def Recursion(n):
    if n > 0:
        abc = n + Recursion(n - 1)
        print(abc)   
    else:
        abc = 0
    return abc

(Recursion(5))


# Factorial Calculation in Recursion


v = int(input("enter a value: "))

def Factorial(v):
    if v == 0:
        return 1
    else:
        return v + Factorial(v - 1)
print(Factorial(v))


#  Fibonacci Sequence 

v = int(input("enter a value: "))

def n(v):
    if v == 0:
        return 0
    elif v == 1:
        return 1
    else:
        return n(v - 1) + n( v - 2)
print((v))

