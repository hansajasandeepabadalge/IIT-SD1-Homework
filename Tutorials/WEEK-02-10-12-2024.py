#Arithmetic Operatorrs
def task1():
    print(8+2*5)
    print((8+2)*5)
    print(20/4)
    print(20//3)
    print(20%3)
    print(2**3)

#Assignment Operators 2
def task2():
    a = 10+5
    b = 30
    b += 5
    print(a, b)

#Arithmetic Assignment Operators
def task3():
    x = 10
    x += 5
    print(x)
    x *= 3
    print(x)
    x -= 2
    print(x)
    x //= 4
    print(x)

#Data Types
def task4():
    print(type(42))
    print(type(3.14))
    print(type(True))
    print(type("Hello, World!"))

#Type Casting
def task5():
    x = "123"
    x = int(x)
    print(x+10)

    y = 50
    y = str(y)
    print("apples" + y)

    z = 3.9
    z = int(z)
    print(z)

#Programming exercises 
#Guided Practice

#Area of a Circle Calculator:
def task6():
    import math

    radius = float(input("Enter the Radius: "))
    area = math.pi * radius ** 2

    print(f"Area of the circle is {area}")

#Salary Increase Calculator:
def task7():
    current_salary = int(input("Enter your Current Salary: "))
    increase_percentage = int(input("Enter your Increase Percentatge: "))

    new_salary = current_salary * (100+increase_percentage) / 100

    print("Your New Salary is " + str(new_salary))

#Volume of a Cylinder:
def task8():
    import math
    
    r = float(input("Enter the Radius of the Cylinder: : "))
    h = float(input("enter the Height of the Cylinder: "))

    v = math.pi * (r ** 2) * h

    print(f"Volume of the Cylinder is {v}")

#Cuboid Area, Perimeter, and Volume Calculator:
def task9():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))

    sur

    
