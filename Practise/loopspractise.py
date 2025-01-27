
#-print 1 to 100

i=1
while i<=100:
    print(i)
    i+=1

#-print 100 to 1
j=100
while j>=1:
    print(j)
    j-=1

#-print multiplication nubmer of nubmer n

n=int(input("Enter a number: "))

k=int(input("Multiplication upto: "))

l=1

while l<=k:
    print(f"{n}x{l} = {n*l}")
    l+=1

#- print the elements of the followint list using a loop [1,4,9,16,25,36,49,64,81,100]


output=[]
x=1
while x<=10:
    output.append(x*x)
    x+=1
print(output)

list=[1,4,9,16,25,36,49,64,81,100]
y=0
while y<len(list):
    print(list[y])
    y+=1

#-search for a number num in this tuple using loop:(1,4,9,16,25,36,49,64,81,100)

num=int(input("Enter number to search: "))
tuple=(1,4,9,16,25,36,49,64,81,100)

m=0
while m<len(tuple):
    if(num==tuple[m]):
        print(f"num is available in index {m}")
        break
    else:
        print("finding")
    m+=1 

#- print odd numbers 

lm=int(input("enter limit for odd numbers: "))
o=1
while o<=lm:
    if(o%2!=0):
        o+=1
        continue
    print(o)
    o+=1


#*For Loop

subjects=["Eng","Science","Maths","Nepali","Social"]

for sub in subjects:
    print(sub)

#- for loop with else

name="bishalkunwar"
for char in name:
    if(char=='k'):
        print("k found")
        break
else:
    print("End")


#--------------
for el in list:
    print(el)


#* Range
#* range(start,stop,step)
#* range(start,stop)
#*range(stop)

seq=range(0,50,3)
for i in seq:
    print(i)
    

#-multiplication table using table

n=int(input("enter a number for multiplication: "))
for t in range(10):
    print(f"{n}x{t}={n*t}")

#-wap to find the sum of first numbers using while

fn=int(input("enter range of  number to add from first: "))
list2=range(fn+1)

b=0
sum=0
while b<=fn:
    sum+=list2[b]
    b+=1
print(f"sum of first {fn} numers is {sum}")

#- Wap to find factorial 
fn=int(input("enter end nubmer to get factorial: "))

b=1
fact=1
while b<=fn:
    fact*=b
    b+=1
print(f"factorial of first {fn} numbers is {fact}")