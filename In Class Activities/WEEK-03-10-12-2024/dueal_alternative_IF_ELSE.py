import random

for i in range(10):
    number = random.randint(0,10)
    print(number)
    if number == 7:
        print("Lucky 7")
    else:
        print("Better luck next time.")