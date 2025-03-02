def type_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args) == data_type:
                func(*args)
            else:
                print(f"{data_type} type required, in {func.__name__}() ")
        return inner_wrapper
    return outer_wrapper

@type_check(int)
def square(n):
    print(n**2)

@type_check(str)
def welcome(name):
    print(f"Welcome,{name}")

square(4)
welcome("bishal")

