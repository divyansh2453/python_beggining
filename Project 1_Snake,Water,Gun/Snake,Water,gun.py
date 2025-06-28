
# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user.
import random as rd
choice={"s":1, "w":2, "g":3}
revchoice={1:"s", 2:"w", 3:"g"}
rev={1:"SNAKE", 2:"WATER", 3:"GUN"}
#greet the Player
# name=input("Your Name ? :")
# print("Hello", name)


user=input("enter your choice :").lower()
computer=rd.choice([1,2,3])
unum=choice[user]
cnum=computer

print(f"U Choose {rev[unum]} \ncomputer choose {rev[cnum]}")
if unum==cnum:
    print("Its a Draw!")
else:
    if unum==1 and cnum==2:
        print("You Won!")
    elif unum==1 and cnum==3:
        print("You Lost!") 
    elif unum==2 and cnum==1:
        print("You Lost!")
    elif unum==2 and cnum==3:
        print("You Won!")
    elif unum==3 and cnum==1:
        print("You Won!")
    elif unum==3 and cnum==2:
        print("You Lost!") 
    else:
        print("Something went wrong!!!!!!")                           
