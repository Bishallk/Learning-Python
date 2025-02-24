

def find_common_elem(n,myList):

    common_elems=[]
    read_elems=[]
    for i in range(n):
        if myList[i] in read_elems:
            common_elems.append(myList[i])
           
        read_elems.append(myList[i])

    return common_elems

myList=[1,2,3,4,5,2,4]
print(myList.sort())
print(f"common elems {find_common_elem(7,myList)}")
print(sorted(myList))

