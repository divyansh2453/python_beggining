# PROJECT 2 – THE PERFECT GUESS
# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random as rd

print("welcome to the number guessing game !")
print("1. play")
opt=int(input("choose your option"))

comp=rd.randint(1, 100)
print("The Computer has chosen its number ..")
user=int(input("your guess :"))
no=0
while user!=comp:
    if user>comp:
        print("lower!")
        user=int(input("your guess :"))
        no+=1
    elif user<comp:
        print("greater!")        
        user=int(input("your guess :"))
        no+=1
print("You Guessed it Right !")
print(f"it took u {no} tries") 
                  
