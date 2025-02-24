def generator():
    i=1
    while i<=200:
        yield i
        i+=1

print(generator())
x=generator()
print(next(x))
print(next(x))
print(list(x))