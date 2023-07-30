#Numbers
#Int
x = 32
print( x + x)
print(type(x))

#float
y = float(x)
print(y + y)
print(type(y))

#complex numbers
cmplx = complex(2, 3)
print(cmplx)

print(type(cmplx))

#Strings

x = "hello"
print(x.upper())

print(x.capitalize())

#string formatting

new_string = f"i am current {y} years old"

print(new_string)

#OR

other = "i am currently {} years old"

print(other.format(y))

#Boolean

a = 32

print( a == 0)

print(a > 10)

#Exercise using a conddition to show how to use a boolean

if(a > 10):
    print("a is greater than 10")

else:
    print(" a  is less than 10")