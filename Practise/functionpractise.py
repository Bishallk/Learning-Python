
#--------Functions--------------


def sum(a,b): #* Normal funcion
    return a+b


def mul(a,b=6): #*default params give default parameter should be given at the end, if some param has no default value then for eg. a has no default value and b has default value . we can't write b as first parameter
    return a*b


#- wap a function to calc factorial

def getUserInput(msg):
    return int(input(msg))


# print(getUserInput("Enter a number: "))

#---------Recursion--------------

def fact(n):
    if(n==0 or n==1): #base case
        return 1
    else:
        return fact(n-1)*n 


# print(fact(3))


#- write a recursive function to calculate the sum of first n natural numbers.

def get_sum(n):
    if(n==1):
        return 1
    else:
        return get_sum(n-1)+n
    
print(get_sum(20))

#- write a fecursive function otoprint all elements in a list. use list and index as params

def get_list(list,index=0):
    if(index==len(list)):
        return
    else:
        print(list[index])
        get_list(list,index+1)

fruits=["mango","orange","Banana","pineapple"]
get_list(fruits)