
#-------- Encapsulation
#* Wrapping data and function into a single unit (Object)

class Account:
    def __init__(self,acc_no,bal):
        self.acc_no=acc_no
        self.bal=bal

    #debit method
    def debit(self,amt):
        self.bal-=amt
        print(f"Rs.{amt} has been debited from A/C {self.acc_no}")
    #credit method
    def credit(self,amt):
        self.bal+=amt
        print(f"Rs.{amt} has been credited to A/C {self.acc_no}")
    def total_balance(self):
        print(f"Yout total balance is: Rs.{self.bal}")

acc1=Account("A1001",100000)
acc1.debit(5000)
acc1.credit(35000)
acc1.total_balance()
        
