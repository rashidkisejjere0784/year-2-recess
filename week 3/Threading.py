#python threading

import threading
import time

def product(a, b):
    sum = 0

    for i in range(b):
        sum += a
        time.sleep(1)
        print(i)

    print("product 1",sum)

def product2(a, b):
    print("product 2",a * b)

t1 = threading.Thread(target=product, args=(5,5))
t2 = threading.Thread(target=product2, args=(5,5))

t1.start()
t2.start()

print("Executing")

t1.join()
t2.join()

print("done")