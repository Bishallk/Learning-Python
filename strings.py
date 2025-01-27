name="bishal kunwar"

#indexing
print(name[0])
print(name[-1])
# slicing
print(name[6:13:2])
print(name[6:13])
print(len(name))

# iterate string
if "i" in name:
    print(True)
else:
    print(False)

for i in range(0,len(name),1):
    print(name[i])


#methods
name.capitalize()
name.format()
name.title()
name.upper()
name.isupper()
name.isnumeric()
name.isdigit()
name.islower()
name.isalpha()
name.find()
name.endswith("al")