# Tutorial 03

# Part 01: Guided Programming Exercises
# Simple Exercise
# If Statement:
def task1():
    user_input = int(input("Enter a number: "))

    if user_input % 5 == 0:
        print("Divisible by 5")

# Else Statement:
def task2():
    user_name = input("Enter your Name: ")
    user_age = int(input("Enter your age: "))

    if user_age >= 18:
        print(f"{user_name}, You are eligible to vote.")
    else:
        print(f"{user_name}, You aren't eligible to vote")

# Elif Statement:
def task3():
    user_input = float(input("Enter a value: "))

    if user_input > 0:
        print("Positive")
    elif user_input < 0:
        print("Negative")
    else:
        print("Zero")

# Nested If-Else Statement:
def task4():
    number = int(input("Enter a number: "))

    if 0 < number < 10:
        if number % 2 == 0:
            print("It's a Even Number")
        else:
            print("It's a Odd Number")
    else:
        print("Enter less than 10 and greater than 0")
        
# Moderate Exercise
# If Statement:
def task5():
    year = int(input("Enter the Year: "))

    if year % 4 == 0:
        print("It's a Leap Year.")

# Else Statement:
def task6():
    character = input("Enter a Character: ")

    if character in "aeiouAEIOU":
        print("It's a Vowel")
    else:
        print("It's a Consonant")
    
# Elif Statement:
def task7():
    character = input("Enter a Character: ")

    if character in "abcdefghijklmnopqrstuvwxyz":
        print("Lowercase")
    elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("Uppercase")
    elif character in "0123456789":
        print("Digit")
    else:
        print("Special Character")

# Nested If-Else Statement:
def task8():
    amount = float(input("Enter your amount: "))

    if amount > 1000:
        dis_amount = amount * (90/100)
    elif 500 <= amount <= 1000:
        dis_amount = amount * (95/100)
    else:
        dis_amount = amount
    print(f"Your discounted amount is Rs.{dis_amount:.2f}")


# Part 02: Unguided Programming Exercises
# Hard Exercise
# Tax Calculator Based on Gross Income
def task9():
    gross_income = float(input("Enter your gross income in £: "))
    
    if gross_income <= 12500:
        tax_owed = 0
    elif gross_income <= 50000:
        tax_owed = (gross_income - 12500) * 0.20
    elif gross_income <= 150000:
        tax_owed = (37500 * 0.20) + (gross_income - 50000) * 0.40
    else:
        tax_owed = (37500 * 0.20) + (100000 * 0.40) + (gross_income - 150000) * 0.45

    net_income = gross_income - tax_owed
    
    print(f"Tax Owed: £{tax_owed:.2f}")
    print(f"Net Income after Tax: £{net_income:.2f}")
    
#Task: Advanced Grade Calculation System
# Get user input and validate it is within the range 0-100
def task10():
    def get_score(score_type):
        score = float(input(f"Enter your {score_type} score (0-100): "))
        while score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            score = float(input(f"Enter your {score_type} score (0-100): "))
        return score

    coursework = get_score("coursework")
    midterm = get_score("midterm")
    final_exam = get_score("final exam")

    final_score = coursework * 0.40 + midterm * 0.25 + final_exam * 0.35

    if final_score >= 70:
        letter_grade = "A"
    elif final_score >= 50:
        letter_grade = "B"
    elif final_score >= 40:
        letter_grade = "C"
    else:
        letter_grade = "F"

    # Display results
    print(f"Final score: {final_score:.2f}")
    print(f"Letter grade: {letter_grade}")

    
    