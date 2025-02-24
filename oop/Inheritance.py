

#----------inheritance
#* When one class(child) derives the properties & mehtods of another class(praent)

## Single  Parent ------> Child
class Car:
    engine="disel"
    @staticmethod
    def start():
        print("started..")
    @staticmethod
    def stop():
        print("stopped")
 
class TyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand   


## Mulilevel Parent ------> Child -----> Child

class Fortuner(TyotaCar):
    def __init__(self,milage):
        self.milage=milage

car1=Fortuner("1000km")

## Multiple  Parent -----> child <-------


class A():  
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

class B(A):
    def __init__(self, x, y, z,e):
        super().__init__(x, y, z)
        self.e=e

class C(B):
    def __init__(self, x, y, z, e,f):
        super().__init__(x, y, z, e)
        self.f=f
objc=C(1,2,3,4,5)
print(objc)

class D(A,B):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
#         # this is multiple inheritance
#         # init function of first class will be called For eg:A

