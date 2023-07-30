# # Syntax Error
# amount = 10000

# if(amount > 1000)
# print("amount greater than 1000")


#Exceptions
# #Division by Zero
# a = 0

# print( 100 / a)

# b = 23
# c = "hello"

# print(b + c)

#Exception Handling

try:
    a = 0

    print(200 / a)
except Exception as e:
    print(f"Exception '{str(e)}' caught")


#Catching specific errors
try:
    a = 9
    b = "some text"

    print( a + b)

except TypeError as e:
    print("Type mistmach error thrown")

#Catching multiple Exceptions

try :
    a = 9
    b = "text"

    print(a + b)

    print(a / 0)

except TypeError as e:
    print("Type mismatch exception")

except ZeroDivisionError as e:
    print("Division By Zero")


#Try, Catch with Else

def Div(a , b):
	try:
		c = (a / b)
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)


Div(3, 3)
Div(2, 0)


#Try Catch Finally
try:
	k = 5/0
	print(k)

except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	print('This is always executed')


#File read and writing
#File writing

file = open("file.txt" , "w")
file.write("helllo")
file.close()

with open("file.txt", "a") as f:
      f.write("\n hello")

#file reading

with open("file.txt", "r") as f:
      print(f.read())