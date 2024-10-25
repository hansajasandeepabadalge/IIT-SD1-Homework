print("Use functions to run separate tasks, for example: task1()")

#Guided Practice Tasks
#Task 1: Basic Arithmetic Operations:
def task1():
    print("3+4")
    print(3+4)
    print("5*6")
    print(5*6)
    print("10/2")
    print(10/2)

#Task 2: Variable Assignments:
def task2():
    x=5
    name="Alice"
    print(x)
    print(name)

#Task 3: Simple Input and Output:
def task3():
    age = input("Enter your age: ") #get age from user
    age = int(age) #convert the input in to an integer value
    print("You are",age,"years old.") #display age

#Task 4: String Concatenation:
def task4():
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name
    print(full_name)

#Task 5: Basic Error Handling:
def task5():
    #print("Hello 
    print("Hello")

#Programming exercises
#Task 6 :Basic Arithmetic Calculator:
def task6():
    x = int(input("Enter the first number: ")) #get first number from user
    y = int(input("Enter the second number: ")) #get second number from user
    
    def addition(): #calculate the addition
        return x + y
    
    def subtraction(): #calculate the subtraction
        return x - y

    def multiplication(): #calculate the multiplication
        return x * y

    def division(): #calculate the division
        return x / y

    #display all the calculations at once
    print(f"Results for the numbers {x} and {y}:")
    print(f"Addition: {addition()}")
    print(f"Subtraction: {subtraction()}")
    print(f"Multiplication: {multiplication()}")
    print(f"Division: {division()}")

#Task 7: Personal Information Script:
def task7():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("Enter your favorite color: ")
    print(f"Hello {name}, you are {age} years old and your favorite color is {color}!")

#Task 8: Unit Conversion Program:
def task8():
    num_of_days = int(input("Enter number of days: "))
    hours = num_of_days * 24 #calculate the hours from number of days
    minutes = hours * 60 #calculate the minutes from number of days
    seconds = minutes * 60 #calculate the seconds from number of days
    print(f"{num_of_days} days is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.") #display all the calculation with a simple note

#Task 9: Simple Interest Calculator:
def task9():
    principal_amount  = int(input("Enter your Principal Amount: "))
    annual_interest_rate = int(input("Enter your Annual Interest Rate (in %): "))
    time_in_years = int(input("Enter your Time (in Years): "))

    SI = (principal_amount * annual_interest_rate * time_in_years)/100 #calculate the Simple Interest with using principal amount, interest rate and time

    print(f"Your Simple Interest is {SI}")

#Unguided Practice Tasks [To be done at home and submitted to BB]
#Task 10: Temperature Conversion:
def task10():
    def celsius_to_fahrenheit(celsius): #conversion of celsius to fahrenheit
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(fahrenheit): #conversion of fahrenheit to celsius
        return (fahrenheit - 32) * 5/9

    def main(): # In this main() function, a user interface is displayed to convert separately
        print("Temperature Converter")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")

        choice = int(input("Enter your Choice: ")) #get user choice

        if choice == 1: 
            celsius = float(input("Enter the Celsius value: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")

        elif choice == 2:
            fahrenheit = float(input("Enter the Fahrenheit value: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")

        else:
            print("Invalid choice.")
    if __name__ == "__main__":
        main()

#Task 11: Grocery Bill Estimator:
def task11():
    item1 = float(input("Enter the price of the 1st Item (in Rs.): "))
    item2 = float(input("Enter the price of the 2nd Item (in Rs.): "))
    item3 = float(input("Enter the price of the 3rd Item (in Rs.): "))

    total = item1 + item2 + item3

    print(f"Total of the three items is Rs.{total}")

#Task 12: Distance Converter:
def task12():
    def  meters_to_kilometers(meters):
        return meters / 1000

    def meters_to_miles(meters):
        return meters / 1609.34

    def main():
        print("Distance Converter")
        print("1. Convert Meters to Kilometers")
        print("2. Convert Meters to Miles")

        choice = int(input("Enter your Choice: "))

        if choice == 1:
            meters = float(input("Enter the Meters value (m): "))
            kilometers = meters_to_kilometers(meters)
            print(f"{meters}m is equal to {kilometers}km")

        elif choice == 2:
            meters = float(input("Enter the Meters value (m): "))
            miles = meters_to_miles(meters)
            print(f"{meters}m is equal to {miles} miles")

        else:
            print("Invalid choice.")
    if __name__ == "__main__":
        main()

#Task 13: BMI Calculator:
def task13():
    weight = float(input("Enter your Weight (in kg): "))
    height = float(input("Enter your Height (in m): "))

    BMI = weight / height ** 2

    print(f"Your BMI value is {BMI}kg/m²")
    if BMI < 18.5: #Display a warrning messages to the user
        print("Warning: You are underweight.")
    elif 18.5 <= BMI < 24.9:
        print("You have a normal weight.")
    elif 25 <= BMI < 29.9:
        print("Warning: You are overweight.")
    else:
        print("Warning: You are obese.")
    
