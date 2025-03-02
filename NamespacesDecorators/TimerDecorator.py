import time

def timer(func):
    def wrapper(*args):
        start=time.time()
        func(*args)
        print(f"Time taken by {func.__name__} : {time.time()-start}secs")
    return wrapper


@timer
def my_function():
    print("I m using timer decorator")
    time.sleep(1)
@timer
def another_function():
    print("I'am also using timer")
    time.sleep(0.5)

@timer
def square(n):
    print(f"Square of {n} is {n**2}")
    time.sleep(0.2)


my_function()
another_function()
square(5)
