
#-----------MODULES 
#* consider module to be the same as a code library.

#* A file containing a set of functions we want ot include in our application.

#* Examples -> math, random, os, time

#* help('modules') ##->prints all module available in system


#-----Math module

import math
print(math.pi)
print(math.factorial(6))
print(math.floor(9.9))


#--------Random module

import random
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))

list=[1,2,3,4,5,6]
random.shuffle(list)
print(list)

#-------Time Module

import time

print(time.time())
print(time.ctime())
# print("sleep",time.sleep(1))


#-----------OS Module

import os
print(os.getcwd()) # current dir
print(os.listdir()) # list dir