#Author: Hansaja Sandeepa
#Date: 5th Oct 2024

'''

Questin: Write a program that converts user-input string
values into integers and performs basic arithmetic (sum, difference, product).

'''

'''
Design
1. Input First Number
2. Input Second Number
3. Caculate the sum
4. calculate the difference
5. calculate the product
6. display sum, difference and product
'''

num1 = int(input("Enter Your First Number: ")) # integer as input
num2 = float(input("Enter Your Second number: ")) # float as input

total = num1 + num2 #sum of two numbers

diff = num1 - num2 #difference of two numbers

prod = num1 * num2 #product of two numbers

print(f"The sum of {num1} and {num2} is {total}\nThe differance of {num1} and {num2} is {diff}\
\nProdcut of {num1} and {num2} is {prod}")
