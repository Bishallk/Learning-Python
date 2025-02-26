class MyException(Exception):
    def __init__(self,msg):
        print(msg)

class Bank:
    def __init__(self,balance):
        self.balance=balance
    
    def withdraw(self, amount):
        if amount <0:
            raise MyException('withdraw amount cannot be negative')
        if self.balance <amount:
            raise MyException(f'Insufficent Balance: Your Current balance is Rs.{self.balance}')
        self.balance=self.balance - amount

obj=Bank(10000)
try:
    obj.withdraw(25000)
except MyException as e:
    pass
else:
    print("Rs.",obj.balance)
