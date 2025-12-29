# wirte a program to check number is possitive nagetive or zero 

a = int(input("enter the value :"))

def result(a):
    if a > 0:
        print(f"{a} is possitive value")
    elif a < 0:
        print(f"{a} is nagetive value")
    else:
        print(f"{a} is zero")
result(a)

