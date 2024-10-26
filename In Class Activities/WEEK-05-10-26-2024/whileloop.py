"""
Exerciese Write a program for guess game

generate a random number ask the user to guess if the guess number user input is larger then
random number tell the user too high if the guess number user input is smaller then random number
tell the user too low if the user get it correct display you got it correct random number and tell
after so many guesses (keep count of number of guesses) range for the random number is 1 to 100

Design

Genarate a random number between 1 and 100
count = 0
guess = nothing
while guess!=number then
    if guess == number then
        print You got it correct after count guesses
    else if guess > number then
        print too high
    else
        prnt too low

"""
import random

ran_num = random.randint(1, 100)
count = 0
user_input = None
while user_input != ran_num:
    count +=1
    user_input = int(input("Guess the number: "))
    if user_input > ran_num:
        print("too high")
    else:
        print("too low")
    
print(f"Yes, You are correct. The correct number is {user_input}.")
print(f"You get {count} counts to guess the correct number.") 