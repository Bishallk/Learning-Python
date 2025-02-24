
#---------Pickling
#* is a process whereby a python object is converted into a byte stream

#---------Unpickling
#* is a inverse operation, whereby a byte stream (from a binary file or bytes like object) is converted back into an object.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"Name: {self.name} age: {self.age}")
        

person =Person("bishal kunwar", 23)

#* pickle dump
import pickle
with open('FileHandling/custom_obj','wb') as f:
    pickle.dump(person,f)

#* pickle load

with open('FileHandling/custom_obj','rb') as f:
    p=pickle.load(f)

p.display_info() #* we can access method that was inside Person class


#* Pickle VS JSON
#* Both are used for serialization and deserialization
#* pickle  lets user to sdotre data in binary format & Json lets user to store data in a human readable format.

#* Pickle wrap our object into binary and send to other and unwrap as obj back which we cannot do in json