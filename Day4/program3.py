# print largest no amout 3 no

a = 98
b = 67
c = 99

def largest_number(a, b, c):
    if a >= b or a >= c:
        print(f"{a} is the largest number")
    elif b >= a and b >= c:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")

largest_number(a, b, c)
