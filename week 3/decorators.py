def do_something(func):

    def inner():

        print("Inner message")

        func()

    return inner

def function():
    print("called function")

f = do_something(function)

f()

print("decorators")

@do_something
def fun():
    print("jhgjgjhg")


fun()


#More decorators

def decorator_func(func):

    def inner(*args):

        print("Inner function")

        result = func(*args)

        return result
    
    return inner

@decorator_func
def sum(a,b,c):
    return a + b + c

@decorator_func
def min(a,b):
    return a - b




print(sum(4,5,6))

print(min(10,4))