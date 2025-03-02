
#-------------D E C O R A T O R S----------|
#* A Decorator is a function that receives another function as a input and adds some functionality(decoration ) to it and returns it.
#* This is only because python function are 1st class citizens

#------Types of decorators
 #* Builtin Decorators -> @staticmethod, @classmethod, @abstractmethod and @property

#* User Defined Decorators -> that programmers can create according to our needs.


#* Example

def my_decorator(func):
    def wrapper():
        print("_______________________")
        func()
        print("_______________________")
    return wrapper


def say_hello():
    print("hello")

a=my_decorator(say_hello)
a()

@my_decorator #* We can use @decorator 
def display():
    print("hello bishal")

display()


#-------Closures
#* Closure is a property in python -> inner function can access properties of outer function even if outer function is removed from memory.

#* Function is removed from  memory after return statement is executed.

#* Decorators are based on this concept ->[closures]

