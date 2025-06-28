# 1. Write a program using functions to find greatest of three numbers.
num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
num3=int(input("enter a number :"))
num4=int(input("enter a number :"))
num5=int(input("enter a number :"))

met=int(input("enter method u want to use 1 or 2 :"))
def great(no1,no2,no3,no4,no5):
    lst=[no1,no2,no3,no4,no5]
    lst.sort()
    result=lst[-1]
    print("greatest number is :",result)

def great2(no1,no2,no3,no4,no5):
    result=max(no1,no2,no3,no4,no5)
    print("greatest number is :",result)

if(met==1):
    great2(num1,num2,num3,num4,num5)
else:
    great(num1,num2,num3,num4,num5)

    

