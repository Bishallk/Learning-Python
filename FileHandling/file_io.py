f=open("demo.txt","r+")
# data=f.read()
line1=f.readline()
f.write("abc")
print(line1)
f.close()
f=open("test.txt","a")
f.write("hello python this is written with file append mode.\n this is next line")


#----with syntax---------------

with open("test.txt","r")as f:
    data=f.read()
    print(data)

#---- delete module------------

import os
os.remove("test.txt")