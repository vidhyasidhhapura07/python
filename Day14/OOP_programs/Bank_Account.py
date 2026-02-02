#  Create a class representing a simple Bank Account.

class BankAccount:
    def __init__(self, Account_Holder_Name, Balance):
        self.Account_Holder_Name = Account_Holder_Name
        self.Balance = Balance

        print(f"👤 Accont Holder {Account_Holder_Name}")

    def Deposit (self, amount):
        self.Balance += amount
        
        print(f"₹ {self.Balance} deposited successfully.")

    def withdraw (self, amount):
        if amount > self.Balance:
            print(f"❌ Insufficient balance.")
        else:
            self.Balance -= amount
            print(f"₹ {amount} withdraw successfully.") 

    def check_balance(self):
        print(f"💰 current blance : ₹{self.Balance}" )  

acc = BankAccount("Niket Rajeshbhai Dodiya" , 100000)
acc.Deposit(1000)
acc.withdraw(500)
acc.withdraw(2000)
acc.check_balance()