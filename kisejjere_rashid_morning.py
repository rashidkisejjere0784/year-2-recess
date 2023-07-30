#Python Operators

#Arithmetic Operators
print("ARITHMETIC OPERATORS")
a = 10
b = 12

#addition
print(a + b)

#subtraction
print(a - b)

#multiplication
print(a * b)

#division
print(a / b)

#integer division
print( a // b)

#modullus
print(a % b)

#exponetion
print(a ** b)

#Assignment Operators
print("ASSIGNMENT OPERATORS")
c = 4

c += 2
print(c)

c -= 2
print(c)

c *= 2
print(c)

c /= 2
print(c)

c //= 4
print(c)


#Comparison Operators
print("COMPARISON OPERATORS")
a = 5
b = 10

print(a == b)

print(a > b)

print(a < b)

print(a != b)

print(a >= b)

print(a <= b)

#Logical Operators
a = 3
b = 10

print(a > 1 and b < 10)


print(a < 1 or b < 10)


print(not(a > 2))

#python identity operators
print("IDENTITY OPERATORS")
a = 4
b = 5
x = [1,2,3,4]
y = [2,3,4,5]

print( a is a)

print( a is b)

print( a is not b)

print(x is y)

print(x is not y)

#MEMBERSHIP OPERATORS
print("MEMBERSHIP OPERATORS")

x = [1,2,3,4,5,6]

print( 2 in x)

print(10 in x)

#BITWISE OPERATORS
print("BITWISE OPERATORS")
a = 10
b = 11

print( a & b)

print(a | b)

print(a ^ b)

print(~a)

print(~b)

print(a << b)

print(a >> b)


#GUI CALCULATOR ASSIGNMENT

import tkinter as tk

expression = ""

def btn_click(num):
    global expression
    expression += str(num)
    text_input.delete(0, tk.END)
    text_input.insert(0, expression)

def btn_clear():
    global expression
    expression = ""
    text_input.delete(0, tk.END)


def btn_equal():
    global expression
    try:
        result = eval(expression)
        text_input.delete(0, tk.END)
        text_input.insert(0, result)

    except:
        text_input.delete(0, tk.END)
        text_input.insert(0, "Invalid operation")

root = tk.Tk()
root.title("Kisejjere rashid calculator")

text_input = tk.Entry(root, width=25)
text_input.grid(row=0, column=0, columnspan=5)
text_input.configure(font=("Arial", 13), borderwidth=5)


#buttons
btn1 = tk.Button(root, text="1", command=lambda: btn_click(1))
btn1.grid(row=2, column=0)
btn1.configure(bg="blue", height=6, width=6)


btn2 = tk.Button(root, text="2", command=lambda: btn_click(2))
btn2.grid(row=2, column=1)
btn2.configure(bg="blue", height=6, width=6)

btn3 = tk.Button(root, text="3", command=lambda: btn_click(3))
btn3.grid(row=2, column=2)
btn3.configure(bg="blue", height=6, width=6)

btn4 = tk.Button(root, text="4", command=lambda: btn_click(4))
btn4.grid(row=3, column=0)
btn4.configure(bg="blue", height=6, width=6)

btn5 = tk.Button(root, text="5", command=lambda: btn_click(5))
btn5.grid(row=3, column=1)
btn5.configure(bg="blue", height=6, width=6)

btn6 = tk.Button(root, text="6", command=lambda: btn_click(6))
btn6.grid(row=3, column=2)
btn6.configure(bg="blue", height=6, width=6)

btn7 = tk.Button(root, text="7", command=lambda: btn_click(7))
btn7.grid(row=4, column=0)
btn7.configure(bg="blue", height=6, width=6)

btn8 = tk.Button(root, text="8", command=lambda: btn_click(8))
btn8.grid(row=4, column=1)
btn8.configure(bg="blue", height=6, width=6)

btn9 = tk.Button(root, text="9", command=lambda: btn_click(9))
btn9.grid(row=4, column=2)
btn9.configure(bg="blue", height=6, width=6)

btn0 = tk.Button(root, text="0", command=lambda: btn_click(0))
btn0.grid(row=5, column=0)
btn0.configure(bg="blue", height=6, width=6)

btnClr = tk.Button(root, text="clr", command=lambda: btn_clear())
btnClr.grid(row=5, column=1)
btnClr.configure(bg="yellow", height=6, width=6)

btnEq = tk.Button(root, text="=", command=lambda: btn_equal())
btnEq.grid(row=5, column=2)
btnEq.configure(bg="red", height=6, width=6)


btnAdd = tk.Button(root, text="+", command=lambda: btn_click("+"))
btnAdd.grid(row=2, column=3)
btnAdd.configure(bg="green", height=6, width=6)

btnSub = tk.Button(root, text="-", command=lambda: btn_click("-"))
btnSub.grid(row=3, column=3)
btnSub.configure(bg="green", height=6, width=6)

btnMul = tk.Button(root, text="*", command=lambda: btn_click("*"))
btnMul.grid(row=4, column=3)
btnMul.configure(bg="green", height=6, width=6)

btnDiv = tk.Button(root, text="/", command=lambda: btn_click("/"))
btnDiv.grid(row=5, column=3)
btnDiv.configure(bg="green", height=6, width=6)

root.mainloop()
