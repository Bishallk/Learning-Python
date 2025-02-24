
#-----------SERIALIZATION---------------|
#*Process of Converting Python Datatypes to JSON Format.


#-Serializtion  using json module
#*List
import json
L=[1,2,3,4,5,6]
with open('FileHandling/demo.json','w') as f:
    json.dump(L,f)


with open('FileHandling/demo.json','r') as f:
    data=f.read()
    print(data)


#----------- Dictionary

d={
    'name':"bishal",
    'age':"23",
    'gender':"male"
}
with open('FileHandling/dict.json','w') as f:
    json.dump(d,f,indent=4)

#-------- Custom Objects

class Person:
    def __init__(self,fname,lname,age,gender):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender

person =Person("bishal","kunwar", 23,"male")

#! python does't support serialization  of custom object by default
#* we can do like this
def show_obj(person):
    if isinstance(person,Person):
        return "{} {} age-> {} gender ->{}".format(person.fname,person.lname,person.age,person.gender)

with open("FileHandling/bishal.json",'w') as f:
    json.dump(person,f,default=show_obj)
    
with open("FileHandling/bishal.json",'r') as f:
    data=f.read()
    print(data)


#------as a dict

def show_obj(person):
    if isinstance(person,Person):
        return {'fname':person.fname,'lname':person.lname,'age':person.age,'gender':person.gender}

with open("FileHandling/bishal.json",'w') as f:
    json.dump(person,f,default=show_obj, indent=4)
    
with open("FileHandling/bishal.json",'r') as f:
    data=f.read()
    print(data)



#-----deserializing

with open("FileHandling/bishal.json",'r') as f:
    d=json.load(f)
    print(d)
    print(type(d)) #dict
