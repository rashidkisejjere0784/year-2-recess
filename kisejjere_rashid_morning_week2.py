class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def Area(self):
        area = self.width * self.height
        return area
    
    def Perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
rect = Rectangle(5, 6)

print("Area is", rect.Area())

print("Perimeter is", rect.Perimeter())



class Converter:
    def __init__(self, conversion_type):
        self._con_type = conversion_type

    def convert(self, value):
        if(self._con_type == "C"):
            F = (value * 1.8) + 32
            return f"{value} to Fahrenheit = {F}"

        elif(self._con_type == "F"):
            C = (value - 32) * (5 / 9)
            return f"{value} to Celsius = {C}"

        else:
            print("Unknown conversion type")



Convert_To_Celsius = Converter("C")

print(Convert_To_Celsius.convert(100))

Convert_To_Fahrenheit = Converter("F")

print(Convert_To_Fahrenheit.convert(100))


#Assignment 2

# Assignment1:  Show encapsulation with employee information to give 
# pay increamentation (Salary with employee information to new_salary)e.g from 850000 to 1000000

class Employee:
    def __init__(self, salary, incrementPercentange = 0.2):
        self._salary = salary
        self._incPerc = incrementPercentange

    def IncrementSalary(self):
        prevSalary = self._salary
        self._salary = prevSalary + (prevSalary * self._incPerc)
        print(f"your Salary {prevSalary} has been incremented to {self._salary}")

    def get_salary(self):
        print("Employee current salary is of",self._salary)


emp1 = Employee(40000)

emp1.get_salary()

emp1.IncrementSalary()

emp1.get_salary()