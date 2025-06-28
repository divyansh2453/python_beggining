# Write a program to find the greatest of four numbers entered by the user.
met=int(input("enter method number 1 or 2 :"))
no1=int(input("enter a number :"))
no2=int(input("enter a number :"))
no3=int(input("enter a number :"))
no4=int(input("enter a number :"))

if met==1:
    great=[no1,no2,no3,no4]
    great.sort()
    print("the greatest numner is :" , great[3])
elif met==2:
    if (no1>no2 and no1>no3 and no1>no4):
        great=no1
    elif (no2>no1 and no2>no3 and no2>no4):
        great=no2
    elif (no3>no2 and no3>no1 and no3>no4):    
        great=no3
    elif (no4>no2 and no4>no3 and no4>no1):    
        great=no4
    print("the greatest numner is :" , great)          