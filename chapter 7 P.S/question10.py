# 10. Write a program to print multiplication table of n using for loops in reversed
# order
n=int(input("enter the number :"))
for i in range (10,0,-1):
    tab=(f"{n} * {i} =",n*i)
    print(tab)