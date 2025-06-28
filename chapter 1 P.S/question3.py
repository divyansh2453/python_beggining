import random

key = random.randint(0, 9)  # Generates a random integer between 0 and 9
choice = int(input("Choose a random integer between 0 to 9: "))  # Correct input usage

if choice == key:  # Use '==' for comparison, not '='
    print("You won!")
else:
    print("Better luck next time.")
