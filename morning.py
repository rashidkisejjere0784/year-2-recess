#Morning Session

#Control Flow
#If Statements

x = 18

if(x < 18):
    print ("Not yet an adult")

elif (x >= 18 and x < 65):
    print("your an adult")

else:
    print("your a real grown up")

#Loops

#Morning Session

#for loop
print("\n\n")
for i in range(10):
    if(i % 2 == 0):
        print(str(i) + " is an even number")

    else:
        print(str(i) + " is an odd number")



#while loop
print("\n\n")

x = 0
while(x < 10):
    print(x )
    x += 1

#Morning Session

#Dictionary creation

pairs = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5
}

#Iteration

for key, value in pairs.items():
    print(key, value)


#Updation

pairs["one"] = 23

print(pairs)

#addition

pairs["six"] = 6

print(pairs)

#deletion

pairs.pop("three")

print(pairs)


#Dictionary Assignment

mental_health_dict = {
    "hello" : "hello how are you feeling today",
    "i feel really sad" : "Am so sorry to hear that but i believe you will get better with time",
    "books are tough" : "My dear jut be patient ypu can make it",
    "thanks" : "Your welcome"
}


text = input("enter in your message : ")

try:
    response = mental_health_dict[text.lower()]

except Exception as e:
    response = "Sorry i dont know what you mean !!"

print(response)