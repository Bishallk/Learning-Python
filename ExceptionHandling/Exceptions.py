
#---------------------------------E X C E P T I O N S ----------------------------------|

#* If things go worng during the execution fo the program(runtime). It generally happens when something unforeseen had happened. 
#* -> Exceptions are raised by python runtime 
#* -> We use Try except block for exception handling

try:
    pass 
    #* This block contains code that might raise an exception

except Exception:
    pass
    #* This block catches exception and handles. this block will execute if there is any exception in try block.

else:
    pass
    #* This block will execute if there is exception in try block.

finally:
    pass
    #* This block will always execute, whether an exception occurs or not.


#*Eg
with open('ExceptionHandling/sample.txt','w')as f:
    f.write("hello world")

try:
    f= open('ExceptionHandling/sample.txt','r') 
except FileNotFoundError:
    print("File not found.")
except FileExistsError:
    print("Cannot divide by zero")
except Exception as e:
    print("Error :",e)
else:
    print(f.read())
finally:
    f.close()
    print("Learning Python")

#----------raise Exception
#* We can manually raise an exception using raise

#* For eg. raise FileNotFoundError("File xain")
#* 

class Bank:
    def __init__(self,balance):
        self.balance=balance
    
    def withdraw(self, amount):
        if amount <0:
            raise Exception('withdraw amount cannot be negative')
        if self.balance <amount:
            raise Exception('Insufficent Balance')
        self.balance=self.balance - amount

obj=Bank(10000)
try:
    obj.withdraw(15000)
except Exception as e:
    print(e)
else:
    print(obj.balance)



