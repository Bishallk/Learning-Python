# tuple is like list but is immutable and can't be changed once created

a=(1,2,3,"hello") #tuple

l=[1,2,23,3,3,"bishal"] #list
x=tuple(l) # list to tuple

#- hard copy soft copy

#-iteration
for i in x:
    print(i)

#-tuple unpacking

b=(1,2,3)
d,e,f=b
print("e:",e)