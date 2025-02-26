class SecurityError(Exception):
    def __init__(self,msg):
        print(msg)
    def logout(self):
        print('you have been logout')
class Account:
    def __init__(self,name,email,password,device):
        self.name=name
        self.email=email
        self.password=password
        self.device=device

    def login(self,email,password,device):
        if device!=self.device:
            raise SecurityError("Somenoe trying to login")
        if email==self.email and password==self.password:
            print("login successful!")
        else:
            print("login Error")




account=Account('bishal','bishalk@gmail.com','bishal2','android')

try:
    account.login('bishalk@gmail.com','bishal2','android')
except SecurityError as e:
    e.logout()
else:
    print(account.name)
finally:
    print('database closed')