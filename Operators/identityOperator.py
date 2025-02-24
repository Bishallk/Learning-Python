
#-----------I D E N T I T Y---------------|
#-----------O P E R A T O R---------------|

#* These operators used to check wheter two objects are of same types or not.
#* And they share same memory location or not.

#* there are 2 identity operators : is & is not # always returns True or False

#*NOTE: Double equals to '==' checks value is same or not but 'is' & 'is not' checks the memory location is same or not.

#- It only works in int, string and None
#* For Eg.
x=10
y=10
print(x is y) # True
z=x
print(z is x) # True
print(id(x)) #140728281594584
print(id(y)) #140728281594584
print(id(z)) #140728281594584

str1="hello"
str2="hello"
print(str1 is str2) # True -until we change the value of str1 or str2

val1=None
val2=None
print(val1 is val2) # True

#- doesn't work in collections like list, tuple, set
list1=[10,20,30]
list2 =[10,20,30]

print(list1 is list2) # False
print(list1 is not list2) # True

