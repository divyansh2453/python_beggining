# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

num=int(input("enter a number :"))

def pat(nm):
    for i in range(nm,0,-1):
        print("*"*i)

pat(num)