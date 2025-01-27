list="1,2,3,4,5,5,345,343,42,342,4,234,"
nums=list.split(",")

for val in nums:
    if(int(val)%2==0):
        print(val)
