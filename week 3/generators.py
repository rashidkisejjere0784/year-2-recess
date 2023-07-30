#generatos are used to avoid memory wastages when accessing data

def infinite():
    i = 0
    while True:
        yield i

for i in infinite():
    print(i , end=", ")