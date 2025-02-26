
#---------------------------------E R R O R S----------------------------------|

#----Syntax Errors
#* These occur when the Python interpreter encounters incorrect syntax.
#* Eg.
#* print("Hello, world"  -> Missing closing parenthesis

#----Indentation Errors
#* These happen when the indentation (spacing at the beginning of a line) is incorrect.
#* Eg.
#* def greet():
#* print("Hello")  -> IndentationError: expected an indented block

#----Name Errors
#* These occours when trying to use varaible or function that hasn't been defined.
#* Eg. print(my_variable) -> my_variable is not defined

#----Type Errors
#* Occurs when an operation is perfomed on an inappropriate data type.
#* Eg. print("Age" + 25) -> TypeError only concatenate str & str (not int)

#----Value Errors
#* Occurs when a function receives an argument of the correct type but invalid value.

#* Eg. int("hello") ->ValueError: invalid literal for int()

#----Index Error
#* Occurs when trying to access an index that is out of range.
#* Eg. my_list=[2,,3,5]
#*     print(my_list[5])

#----Key Errors
#* Occur when trying to access a dictionary key that doesn't exist.
#* Eg. my_dict={"name":"Bishal"}
#*     print(my_dict["age"]) -> KeyError : 'age'

#---- Attribute Errors
#*  Occour when trying to access an invalid attribute of an object.
#* Eg. num= 30
#*     num.append(5) -> int obje has no attribute 'append'

#---- ModuleNotFound Errors
#*  Occurs when trying to import a module that does't exist.
#* Eg. import bishal -> No module named 'bishal'

#---- Import Errors
#* Occurs when an imported module exist but has issues.
#* Eg. from math import square -> cannot import name 'square' from 'math'

#---- FileNotFound Errors
#* Occurs when trying to open non-existent file
#* Eg. f= open('abc.png') -> No such file or directory

#---- ZeroDivision Errors
#* Occurs when dividing by Zero '0'
#* Eg. print(30/0) -> division by zero


