#Inheritance

class Animal:
    def make_sound(self):
        print("Animal makes sound")

class Cat(Animal):
    def make_sound(self):
        print("Cat makes sound")


    

animal = Animal()
cat = Cat()

animal.make_sound()
cat.make_sound()

#Multple Inheritange
class Flyable:
    def fly(self):
        print("I am flying")


class Bird(Animal, Flyable):
    pass

bird = Bird()
bird.fly()
bird.make_sound()

#Polymorphism
class Dog(Animal):
    def make_sound(self):
        return "Wooof"
    

class Snake(Animal):
    def make_sound(self):
        return "siiiiii"
    

dog = Dog()
snake = Snake()

dog.make_sound()
snake.make_sound()

#Method Overriding

class Shape:
    def Area(self, width, length):
        print("Shape area is = ", (width * length))

class Rectangle(Shape):
    def Area(self, width, length):
        print("Recatangle Area is = ", (width * length))

rect = Rectangle()

rect.Area(20, 32)

#Abstraction
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def Print(self):
        pass

class B(A):
    def Print(self):
        return "Hello"
    

b = B()

print(b.Print())

#Assignment
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext

def print_receipt():
    store_name = entry_store_name.get()
    address = entry_address.get()
    transaction_details = text_transaction_details.get("1.0", "end-1c")
    
    # Check if any required field is empty
    if not store_name or not address or not transaction_details:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    # Generate the receipt content
    receipt = "==== RECEIPT ====\n"
    receipt += "Store Name: {}\n".format(store_name)
    receipt += "Address: {}\n".format(address)
    receipt += "Transaction Details:\n{}\n".format(transaction_details)
    receipt += "=================\n"
    
    # Create a new window to display the receipt
    receipt_window = tk.Toplevel()
    receipt_window.title("Receipt")
    
    # Display the receipt content in a label
    receipt_label = tk.Label(receipt_window, text=receipt, justify=tk.LEFT, padx=10, pady=10)
    receipt_label.pack()
    
    # Reset the fields
    entry_store_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    text_transaction_details.delete("1.0", tk.END)

# Create the main window
window = tk.Tk()
window.title("Receipt Printing Program")

# Store Name
label_store_name = tk.Label(window, text="Store Name:")
label_store_name.pack()
entry_store_name = tk.Entry(window)
entry_store_name.pack()

# Address
label_address = tk.Label(window, text="Address:")
label_address.pack()
entry_address = tk.Entry(window)
entry_address.pack()

# Transaction Details
label_transaction_details = tk.Label(window, text="Transaction Details:")
label_transaction_details.pack()

# Add scrolling to the text box
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_transaction_details = scrolledtext.ScrolledText(window, height=5, width=30, yscrollcommand=scrollbar.set)
text_transaction_details.pack()

# Attach the scrollbar to the text box
scrollbar.config(command=text_transaction_details.yview)

# Print Button
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.pack()

# Reset Button
def reset_fields():
    entry_store_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    text_transaction_details.delete("1.0", tk.END)

reset_button = tk.Button(window, text="Reset Fields", command=reset_fields)
reset_button.pack()

# Save Receipt to File
def save_receipt():
    store_name = entry_store_name.get()
    if not store_name:
        messagebox.showerror("Error", "Please enter the store name.")
        return
    
    receipt = "==== RECEIPT ====\n"
    receipt += "Store Name: {}\n".format(store_name)
    receipt += "Address: {}\n".format(entry_address.get())
    receipt += "Transaction Details:\n{}\n".format(text_transaction_details.get("1.0", "end-1c"))
    receipt += "=================\n"
    
    file_name = "{}_receipt.txt".format(store_name.lower().replace(" ", "_"))
    with open(file_name, "w") as f:
        f.write(receipt)
    messagebox.showinfo("Success", "Receipt saved to {}".format(file_name))

save_button = tk.Button(window, text="Save Receipt", command=save_receipt)
save_button.pack()

# Load Receipt from File
def load_receipt():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return
    
    with open(file_path, "r") as f:
        receipt_content = f.read()
    
    # Display the receipt content in the text box
    text_transaction_details.delete("1.0", tk.END)
    text_transaction_details.insert("1.0", receipt_content)

load_button = tk.Button(window, text="Load Receipt", command=load_receipt)
load_button.pack()

# Run the main window
window.mainloop()
