 #-Dictionary is also like list is mutable
 #- it is iterable but it has some special powers and those are keys and values
#- focus on code part you will get it

d={1:"sunday",2:"monday",3:"tuesday",4:"wednesday"}
print(len(d))
print(d[2])
d[5]="thursday"

e={5:"thursday",6:"friday",7:"saturday"}
d.update(e)

for i in d:
    print(d[i])