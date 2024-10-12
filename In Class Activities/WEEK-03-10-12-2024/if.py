#Genrate a random number 10 times each time cheak if it is 7 if it is 7 then print "Luck 7" otherwise print the number irrespective 7 or not 7.
import random

for i in range(10):
    number = random.randint(0,10)
    print(number)
    if number == 7: #single alternative if
        print("Lucky 7")
        
    