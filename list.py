
#-list is a versatile mutable data structure that allows you to store a collection of items.
x="hello py"
#list indexing
a=[20,40,50,60,"bishal",True,len(x) ]
print(a)
print(a[3])
# list slicing
print(a[0:4])

a[0]=100
print(a)
#- list is mutable and every element can be changed accordingly

#- iterating over list is similar to strings
for i in range(0,len(a)):
    print(a[i])

#-methods
a.append(3)
a.insert(1,222)
a.pop(2) #index
a.remove(60) #item