# The __init__() Method

# class person:
#     def __init__(self, name):
#         self.name = name

# p1 = person("Niket Dodiya")

# print(p1.name)

# # Create a class without __init__():

# class person():
#     pass

# p1 = person()
# p1.name = "Niket Dodiya"
# p1.age = 25

# print(p1.name)
# print(p1.age)

# # Default Values in __init__()

# class person():
#     def __init__(self, name, city, age=25 ):
#         self.name = name 
#         self.age = age 
#         self.city = city      

# p1 = person("Niket", "Surat")
# p2 = person("Vidhya", "Surat", 23)

# print(p1.name, p1.city, p1.age)
# print(p2.name, p2.city, p2.age)


# # The self Parameter

# class person():
#     def __init__(self , name, age):
#         self.name = name 
#         self.age = age 

#     def info(self):
#         print("My Name is " + self.name)
    
# p1 = person("Niket r. dodiya" , 25)
# p1.info()


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")

acc = BankAccount("Niket", 1000)

acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)
acc.check_balance()


# ---- ATM Menu ----
# name = input("Enter account holder name: ")
# account = BankAccount(name, 0)

# while True:
#     print("\n===== ATM MENU =====")
#     print("1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         account.check_balance()

#     elif choice == "2":
#         amount = int(input("Enter amount to deposit: "))
#         account.deposit(amount)

#     elif choice == "3":
#         amount = int(input("Enter amount to withdraw: "))
#         account.withdraw(amount)

#     elif choice == "4":
#         print("🙏 Thank you for using the ATM. Goodbye!")
#         break

#     else:
#         print("⚠️ Invalid choice. Please try again.")

