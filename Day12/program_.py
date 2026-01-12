# # simple Try & Except Block

# try :
#     print (v)
# except :
#     print("error...! ")

# # NameError with try and except block

# try :
#     print(n)
# except NameError:
#     print("variable is not define")
# except :
#     print("Error...!")

# # ValueError with try and except block

# try :
#     n = int(input("enter a value: "))
#     print(f"The number you entered is {n}.")
# except ValueError:
#     print("Invalid Value...!")

# # ZeroDivisionError with try and except block

# try :
#     num1 = int(input("enter a value: "))
#     num2 = int(input("enter a value: "))
#     result = ( num1 / num2)
#     print("result" , result)
# except ZeroDivisionError:
#     print("You can’t divide by zero!")
# except:
#     print("That’s not a valid number.")    

# # NameError with try and except block

# try:
#     print(v)
# except NameError:
#     print("veriable v is not define")
# except:
#     print("somthing else went wrong")

# # try & except & else Block

# try:
#     print("Hello")
# except:
#     print("abcd")
# else:
#     print("True")

#  # raise 

# x = -1 

# if x < 0:
#     raise Exception ("please enter possitive value")

# raise 2

# x = "Hello"

# if not type(x) is int :
#     raise TypeError ("Only Allow for Integer Value")

# try except else or finally block 

# try :
#     x = 70
#     print(x)
# except:
#     print("error...! ")
# else:
#     print("True")
# finally:
#     print("finished")
