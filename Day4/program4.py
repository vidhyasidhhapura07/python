#  person is aligable for vote or not

a = int(input("enter value :"))

def value(a):
    if a > 18:
        print(f"{a} is aligable for vote")
    else:
        print(f"{a} is not aligable for vote")
value(a)