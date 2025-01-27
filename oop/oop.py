# #class 
# class Vehicle:
#     def __init__(self,name,color,price):
#         self.color=color
#         self.price=price
#         self.name=name
#     def race(self):
#         print(self.name,"racing")

# car=Vehicle("car","black",120000)
# bike=Vehicle("bike","red",60000)
# print(car.color)
# print(bike.color)
# bike.race()

# #inheritance

# class A():
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z




# class B(A):
#     def __init__(self, x, y, z,e):
#         super().__init__(x, y, z)
#         self.e=e


# class C(B):
#     def __init__(self, x, y, z, e,f):
#         super().__init__(x, y, z, e)
#         self.f=f
#     #this is multilevel inheritance c can access properties of A& B
# objc=C(1,2,3,4,5)
# print(objc)

# class D(A,B):
#     def __init__(self, x, y, z):
#         super().__init__(x, y, z)
#         # this is multiple inheritance
#         # init function of first class            will           be        called For eg:A


#ploymorphism

class Animal:
    def __init__(self,name):
        self.name=name
    
    def showname(self):
        print(self.name)
class Human:
    def __init__(self,name):
        self.name=name
    def showname(self):
        print(self.name)
ob= Human("bishal")
print("name",ob.showname())