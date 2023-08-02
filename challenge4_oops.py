class Account:

    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
       

class SavingsAccount(Account):

    def __init__(self,title,balance,interest):
        super().__init__(title,balance)
        self.interest=interest
       
obj=Account("Ashish",5000)
obj1=SavingsAccount("ashish",5000,5)

print(obj.title)
print(obj.balance)
print(obj1.title)
print(obj1.balance)
print(obj1.interest)

