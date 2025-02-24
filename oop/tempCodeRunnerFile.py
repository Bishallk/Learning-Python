class User:
    def __init__(self,uname,pwd):
        self.uname=uname
        self.__pwd=pwd
        

u1= User("bishal","all1234") 

print(u1.__pwd)