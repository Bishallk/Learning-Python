
#---------------------- C L A S S --------------------|

#* Class is a blueprint for creating obejcts.
#* Syntax -> class Classname:
                    #* consturctor
                    #* attributes
                    #* methods

#* Creating Object or Instance
#* obj= Classname()

#-----Constructors
#* All classes have a function called __init__() which is always executed when the class is begin initiated.
#* consturctor __init__(self,..,..) alwalys takes self parameter
## Default constructor -> having only self param

## Parameterized constructor -> having self & other multiple params

#-----self parameter
#* self parameter is a reference to the current instance of class & is used to access the variables in class

#*Example

class Vehicle:
    def __init__(self,name,color,price): #* -->constructor
        self.color=color
        self.price=price
        self.name=name
    def race(self):#* ->must pass self param in other methods as well
        return "racing"

car=Vehicle("car","black",120000)
bike=Vehicle("bike","red",60000)
print(car.color)
print(bike.color)
bike.race()

#---------- Class & Instance Attributes
#* Class attributes are those attributes which are common to all objects or instances. For example college_name is common for all students of particular college.
class Student:
    college_name="programming college"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def get_student_details(self):
        return f"name: {self.name} roll no.: {self.rollno}"
    

#* Instance attributes are those which are different to every objects or instances. For example roll_no is different for every students.
#* we need to use self.roll_no to get rollno of student.

student1=Student("student1",1)


#----------- Static method
#* methods that don't use self param (works at class level)
#* we use @staticmethod decorator
class Person:
    @staticmethod
    def hello():
        print ("Hello")

Person.hello()

#-------- Abstraction 
#* Hiding the implementation details of class and only showing the essential features to  the user.

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started")

c1=Car()
c1.start()

#------- del keyword
#* we can use del keyword to delete object propertied or object itself
#* For Eg.
class Account:
    def __init__(self,no,bal):
        self.no=no
        self.bal=bal
acc2=Account("A1002",4000)
print(acc2.bal)
del acc2.bal #delete attribute
print(acc2.bal)

print(acc2)
del acc2    # delete object
print(acc2)


#----- Private attribute and methods
#* Conceptual Implementaion in python
#* Private attributed & methods are meant to be used only within the class and are not accessible from outside the class.
class User:
    def __init__(self,uname,pwd):
        self.uname=uname
        self.__pwd=pwd
    

u1= User("bishal","all1234") 

print(u1.__pwd) #


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

