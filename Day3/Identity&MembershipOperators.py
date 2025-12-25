# IDENTITY OPERATOR

N = ["mango", "apple"]
V = ["mango", "apple"]
D = N

# is operator (both variables are the same object Returns True)

print("D is the same object as N =" ,N is D) # true
print("N is not the same object as V" , N is V) #flase
print("use Equal to opertore" , N == V) # true

#is not operator (both variables are not the same object Returns True)

print(N is not D)# false
print(N is not V)# true
print(N != V)# flase 


# MEMBERSHIP OPERATOR

#in operator

P = ["mango","banana","apple","guava","pear"]
print("pear" in P) # true

# not in operator

print("pear" not in P) #false 