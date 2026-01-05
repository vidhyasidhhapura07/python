v= int(input("enter a value : "))

def n(v):
    if v == 0 or v == 1:
        return 1
    else:
        return v * n(v - 1)
print(n(v))

#  # prime number

# def n(v):
#     if v <= 1:
#         return False
#     for d in range(2, v):
#         if v % d == 0:
#             return False
        
#     return True

# p = int(input("enter a number : "))

# if n(p):
#     print(f"{p} is a prime number")
# else:
#     print(f"{p} is not a prime number")

# # square

# n = int(input("Enter a number: "))

# def a(b):
#     for c in range(n):
#         return n * n # x = n * n
#         # return x
# print("square is :" ,a(n))