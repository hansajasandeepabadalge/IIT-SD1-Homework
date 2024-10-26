# Tutorial 04: Introduction to Loops
# Guided Practice:
# Simple Questions
# Question 1: Printing Numbers with a For Loop
def task1():
    for i in range(1,6):
        print(i)

# Question 2: Counting Down with a While Loop
def task2():
    count = 5
    while count>=1:
        print(count)
        count-=1

# Question 4: Simple Sum with a While Loop
def task3():
    count = 0
    total = 0
    while count < 5:
        count += 1
        total = total + count
    print(total)
    
# Moderate Questions
# Question 4: Sum of Even Numbers
def task4():
    total = 0
    for i in range (1,5):
        even_number = 2*i
        total = total + even_number
    print(total)

# Question 5: User Input Loop
def task5():
    total = 0
    while True:
        user_input = int(input("Enter a number: "))
        if user_input > 0:
            total = total + user_input
        else:
            print(f"Total is {total}")
            break



# Question 6: Multiplication Table
def task6():
    user_input = int(input("Enter your nuumber to show the multiplication table related to that number: "))
    for i in range (1,11):
        mul = i * user_input
        print(f"{i} x {user_input} = {mul}")





# Unguided Practice (Try at home)
# Question 7: Factorial Calculation
def task7():
    n = int(input("Enter a number: "))
    num = n
    factorial = 1
    while 0 < n:
        factorial = factorial * n
        n-=1
    print(f"{num}! = {factorial}")
    
# Question 8: Finding Prime Numbers
    
def task9():
    for i in range(1,6):
        for j in range (1,6):
            print(i*str(j))
            
    