
#-------------------- F U N C T I O N S -------------------------------#


def hello():
    print("hello")

hello()


#------default parameter
def hello2(a,b,c,d=2):
    print(a,b,c,d)

hello2(2,3,4,5) 



#-----return keyword
def evenodd(a):
    if a%2==0:
        return("even")
    else:
        return("odd")
    

#----ploymorphism
def multiply(p1,p2):
    return p1*p2

print(multiply(1,5))
print(multiply("a",5))
print(multiply(4,"y"))


#---------Lambda function
cube= lambda x: x**3
print(cube(5))

multiply= lambda x,y:x*y
print(multiply(4,5))


#- def function(*args) 
#* (*args) allows us to pass mulitple parameters 
def sum_all(*args):
    print(args)
    return sum(args)

print(sum_all(2,3,4,6,34,53,5,34,34))

#------keyword parameter
hello2(d=30,b=2,a=5,c=20) 


#- def function (**kwargs)
#* allows you to pass a variable number of keyword arguments (i.e., key-value pairs) to a function.
#* It is used when you don’t know in advance how many or which keyword arguments will be passed.
#* Inside a function, **kwargs is treated as a dictionary where the keys are argument names, and the values are their corresponding values.
#* For Eg.
def example_function(**kwargs):
    print(kwargs)

example_function(a=1, b=2, c=3)  # Output: {'a': 1, 'b': 2, 'c': 3}

#- usecases
#*When the number of keyword arguments is not fixed.
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25, location="NY")

#*Useful when creating objects dynamically.
class Person:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

person = Person(name="John", age=28, location="CA")
print(person.name, person.age, person.location)
# Output: John 28 CA

#* **kwargs is a dictionary, so methods like .items(), .get(), etc., are useful.
#* we should follow this signature when we use both *args and **kwargs

def func(positional, *args, **kwargs):
    pass

#*For Eg.
def myfunction(a, b, *args, **kwargs):
    print("a:", a) # a: 1
    print("b:", b) # b: 2
    print("args:", args) # args: (3, 4)
    print("kwargs:", kwargs) # kwargs: {'x': 5, 'y': 6}

myfunction(1, 2, 3, 4, x=5, y=6) ## calling functions and passing args and keyword args


#* yield keyword
#*  the yield keyword is used in a function to turn it into a generator.A generator is a special type of iterable that generates values one at a time as they are needed, rather than all at once.

def generator():
    i=1
    while i<=10:
        yield i
        i+=1

print(generator())
x=generator()
print(next(x))
print(next(x))
print(list(x))