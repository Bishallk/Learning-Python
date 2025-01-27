with open("practise.txt","w")as f:
    f.write("Hi everyone \n we are learning python and we will learn java next")


with open("practise.txt","r")as fi:
    data=fi.read()

new_data= data.replace("java","javascript")
print(new_data)


with open("practise.txt","r") as f:
    data=f.read()
    print(data.find("learning")) #-returns index if found
    print(data.find("hello")) #- returns -1 if not found
    if(data.find("learning")!=-1):
        print("found")
    else:
        print("not found")



list="1,2,3,4,5,5,345,343,42,342,4,234"
nums=list.split(",")

for val in nums:
    if(int(val)%2==0):
        print(val)

