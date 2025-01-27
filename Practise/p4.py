
#-WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#- an empty dictionary & add one by one. Use subject name as key & marks as value.

marks={}

s1=int(input("Enter mark of Physics:"))
marks.update({"Phy":s1})
s2=int(input("Enter mark of Chemistry:"))
marks.update({"Chem":s2})
s3=int(input("Enter mark of Maths:"))
marks.update({"Maths":s3})

print(marks)


#- find way to store 9 & 9.0 sepreatly in set

x=9
y=str(float(x))

set={x,y}
print(set)
set2={9,"9.0"}
print(set2)

set3={
    (1,"int"),
    (1.0,"float")
}
print(set3)
