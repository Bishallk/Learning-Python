def outer():
    u=1
    def inner():
        nonlocal u
        u+=1
        print('inner',u)
    inner()
    print('outer',u)

outer()