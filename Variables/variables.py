
#--------------------------------------- S T A R T -------------------------------------------------|
#------------------------------------------ O F ----------------------------------------------------|
#------------------------------------ V A R I A B L E S --------------------------------------------|


#* Defination--> variable is a name given to a memory loction in a program. 
#* Syntax--> variable_name= value 

#--------------------------------->IMP NOTES TIPS & TRICKS <---------------------------------------|
#* 1. If Different Variables have same value, then all of them will point same memory location.
#* For Eg.
a=10
b=a #b=a=10
c=10 ## All of them will point same meomory location instead of creating new memory location.

#* 2. There is a function id(variable) to get memory address of variable.
#* Eg.
print(id(a)) #140707708205784
print(id(b)) #140707708205784 ## They all have same Memory location.
print(id(c)) #140707708205784

#* 3. There is no Built in way to make a variable Constant in python. Theere is a convention 
#*    ie. define variable using UPPERCASE letters.
#* For Eg.
PI=3.14
GRAVITY=9.8 ## They are not actually constant, this is convention to define Constant variables.


#* 4. There is a function type(variable) to get type of variables.
#* For Eg.
print(type(a)) #output: <class 'int'>


#* 5. We can Assign Multiple Variables in One line 
#* For Eg.
x, y, z = 5, "Bishal", 3.14 ## Assign multiple variables at same line
print(a, b, c)

x = y = z = 10 ## Assign the same value to multiple variables
print(x, y, z) 

#* 6. We can swap variable values easy without needing a temporary variable.
#* For Eg.
x, y = 5, 10
x, y = y, x
print(x, y)  # Output: 10, 5

#* 7. Scope of Variables declared inside a function are local by default.
#*    Scope of Variables declared outside functions are global.
#* For Eg.
x = 10  # Global variable

def function():
    x = 5  # Local variable
    print("Inside:", x)

#* 8. we can use the 'global' keyword to modify a global variable inside a function.
#* For Eg.

def function():
    global x #Global Variable
    x = 20

#* 9. Type hinting help specify the type of a variable
#* For Eg.
age: int = 25
name: str = "Bishal" ## Type Hinting
height: float = 5.8

#* 10. python automatically deletes variables that are no longer used to free memory.
#* We can use 'del' to delete variables manually if needed
#* For Eg. 
d = 10
del d

#* 11. Single Leading Underscore (_variable): For internal use or weak "private" indication.
#* This is a convention and doesn’t enforce strict privacy 
#* For Eg.
class MyClass:
    def __init__(self):
        self._internal_value = 42  # Weak "private" variable

    def display(self):
        print(f"The internal value is: {self._internal_value}")

obj = MyClass() #* Creating an instance of the class

#* Accessing the internal variable through a method (recommended)
obj.display()  # Output: The internal value is: 42

#* Accessing the internal variable directly (not recommended)
print(obj._internal_value)  # Output: 42

#* 12. Double Leading Underscore (__variable): For name-mangling in classes.
#* [Name mangling] is a mechanism in Python that modifies the names of variables that have a double leading underscore (__variable) to include the class name as a prefix. This is done to avoid name conflicts in inheritance scenarios or when subclassing.
#* For Eg.
class MyClass:
    def __init__(self):
        self.__private_var = 42  #! Name-mangled

    def get_private_var(self):
        return self.__private_var

obj = MyClass()
print(obj.get_private_var())  # Output: 42 ## Accessing through a method (preferred)


#* Direct access (will raise an error)
#* print(obj.__private_var)  # AttributeError: 'MyClass' object has no attribute '__private_var'


print(obj._MyClass__private_var)  #Output: 42 ## Accessing the mangled name

#* What Happens in Name Mangling ??

#-> The variable __private_var becomes _MyClass__private_var internally.
#-> We can still access the variable using the mangled name (_MyClass__private_var), so it’s not truly private
#-> Name mangling is designed to avoid accidental access or overriding in subclasses, not for enforcing true privacy.


#* 13. Single Underscore (_): Often used as a "throwaway" variable in loops or unpacking
#* It’s a convention to indicate that you’re ignoring the variable.

#* When we don’t need the loop variable we can use underscore '_' in place of variable:
#* For Eg.
for _ in range(5):
    print("Hello!")  ## We're ignoring the loop variable

#*When unpacking tuples, lists, or other iterable objects, use underscore '_' for values we want to ignore:
#* For Eg.
x, _, z = (1, 2, 3)  ## Ignore the second value
print(x, z)  # Output: 1 3

#*Using underscore '_' as a placeholder for temporary or dummy values:
#*For Eg.
_ = "I don't need this value"


#* In the Python interactive shell, undersocre '_' holds the result of the last executed expression
#* Eg.
#>>> 10 + 20
#>>> 30
#>>> _
30 #output  ## Underscore holds the last result

#--------------------------------------------- E N D --------------------------------------------------|
#---------------------------------------------- O F ---------------------------------------------------|
#--------------------------------------- V A R I A B L E S --------------------------------------------|


