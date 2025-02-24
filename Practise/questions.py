#strong number programme
# 145
# 1!+4!+5!
# 1+24+125=145

 #-> strings questions
a="hello python"
print(a.upper())
print(a.lower())
print(len(a))

#reverseing string
b=""
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
    
print(b)


# or
print(a[::-1])


# arange string characters such that lower case should come first in another string

a="BIshaL KunwAr"
b=""
for i in a:
    if(i.islower()):
        b=b+i
for i in a:
    if(i.isupper()):
        b=b+i


print(b)
print(a.split())
