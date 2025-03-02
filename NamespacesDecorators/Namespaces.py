

#* A namespace ia a space that holds names(identifiers). Programatically, namespaces are dictionary of identifiers(keys) and their objects(values)

#-----Types of Namespaces

#* Built in Namespaces

#* Global Namespaces

#* Enclosing Namespaces

#* Local Namespaces


#--------Scope 

#* Scope is a textual region of a python program where a namespace is directlry accessible.

#-------LEGB rule
#-> Local-> Enclosed -> Global -> Builtin
#* Ther interpreter searches for an name from inside out, looking in the local, enclosing, global, and finally the built-in scope. 

#* If the interpreter doesn't find the name in any of these locations, then python raise a NameError Exception.


#* Eg.
#* local & global variable

a=2

def func():
    b=5
    print(b)

print(a)
func()

#* same name for local and global varibale

a=2
def func1():
    a=3
    print(a)

print(a)
func1()

#*local and global ->edit global variable
a=2
def func2():
    #global a #* we can edit this using global a
    #a+=1  #* gives error
    print(a)

func2()
print(a)

#* local and global ->global created inside local
def func3():
    global x
    x=11
    print(x)

func3()
print(x)

#* local and global ->function parameter is local

j=70 
def func4(z): #z becames local varibale
    print(z)

func4(55)  
print(j)
# print(z) #* Gives NameError z

#--------builtins
import builtins
print(dir(builtins))


L=[1,3,5,6,7,77]
print(max(L)) #max() is built in function

#* renameing built-ins

def max():
    print("hello") # this will override builtin functionality

li=[1,3,5,6,7,77]
# max(li) #* Gives Error
max() #hello

#! we need to careful while defining function name


#-----------Enclosing Scope

i=12
def outer():
    i=10
    ## enclosing scope
    def inner():
        ## Local scope
        i=15
        print("inner function")
        print(i)   # will print 15
    inner()
    print('outer function')

outer()

print("main function") ##Global Scope


#-------------nonlocal keyword
#* is used to  access eclosing socpe

def outer():
    u=1
    def inner():
        nonlocal u
        u+=1 # will also change outer variable
        print('inner',u)
    inner()
    print('outer',u)

outer()