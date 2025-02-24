
#----------M E M B E R S H I P-------------|
#-----------O P E R A T O R----------------|

#* These opetators used to test wheter a specific value or item is present within sequence , such as string, list tuple or set.

#* There are 2 membership operators: 'in' & 'not in'
#* Returns True & False as output

#* For Eg.

list1=[1,2,4,3,5]
print(3 in list1) # Ture
print(33 in list1) # False
print(33 not in list1) # Ture

user_list=["bishal","amrit","biksah"]
name=input("Enter your name: ")
if name in user_list:
    print("Access granted")
else:
    print("Access Denied")
