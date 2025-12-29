
# check number is possitive , negative or zero and further check positive number is odd ya even

N = int(input("enter any number : "))

def V(N):
    if N > 0:
        print(f"{N} is possitive value.")
        if N % 2 == 0:
            print(f"{N} is even number.")
        else:
            print(f"{N} is odd number.")
    elif N < 0:
        print(f"{N} is negative value")
    else:
        print(f"{N} is Zero")
V(N)


#  check the age for aligable drive or not and further check aligable for vote 

V = 22
N = 17

def N_v(V):
    if V > 20:
        print(f"{V} is aligable for drive") 
        if N > 18:
            print(f"{N} is aligable for vote")
        else:
            print(f"{N} is not aligable for vote")
    else:
        print(f"{V} is not aligable for drive") 
N_v(V)