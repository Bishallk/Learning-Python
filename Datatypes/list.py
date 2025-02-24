
#--------------------- L I S T ------------------------------#
#----------------- D A T A T Y P E --------------------------#

#*list is a versatile mutable data structure that allows you to store a heterogeneous elements(different data types).

my_list = [1, "Hello", 3.14, True]  #with mixed data types
my_list = [1,2,3,4,5,6,7,87,]
#----- list indexing
a=[20,40,50,60,"bishal",True]
print(a)
print(a[3])
#----- list slicing
print(a[0:4])

a[0]=100
print(a)

#------- List Comprehension
#*For Eg. if we want to add 2 marks we can do like this in short
my_marks=[20,30,46,67]
new_marks=[x+2 for x in my_marks]
print(new_marks)

#* Another Eg. find cube of numbers in range.
#* Using loop
cubes=[]
for x in range(10):
    if x % 2==0:
        cubes.append(x**3)
print("Using for loop : ",cubes)

#* using list comprehension
new_cubes=[x**3 for x in range(10) if x%2==0]
print("Using list comprehension : ",new_cubes)


#- list is mutable and every element can be changed accordingly

#- iterating over list is similar to strings
for i in range(0,len(a)):
    print(a[i])

#-methods
#* append(elem) -> add single element
#* extend(elem,elem2) -> add multiple elements

a.insert(1,222)
a.pop(2) #index
a.remove(60) #item