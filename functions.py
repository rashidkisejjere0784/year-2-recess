#Functions
#blank functions
def func():
    print("Say hello")

func()
def func_with_args(x):
    print("you have passed argument", x)

func_with_args(10)

#function with return types
def add(x, y):
    print((x + y))

add(32, 21)


#modules as, from

import module

module.saySomething()

module.product(4, 6)

#using the from

from module import product

product(5, 7)


#input and output

x = input("Enter in a value")

print(x)

#inputting multple values

y = map(int, input("Eneter in values: ").split())

for x in y:
    print(x)


