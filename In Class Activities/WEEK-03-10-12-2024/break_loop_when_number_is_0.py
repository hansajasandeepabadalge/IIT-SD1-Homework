#Get a Random number between o and 10 until 0 is genarated as a random number
#print the number if the number is 7 print lucky 7

#you cannot use endless loop or beak statement

import random

number = None
count = 0
while number != 0:
    number = random.randint(0,10)
    if number == 7:
        count += 1
        print("Lucky Number")
    else:
        count += 1
        print(f"The number {count} is {number}")
    