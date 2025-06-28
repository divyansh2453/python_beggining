# 6. Write a program to calculate the factorial of a given number using for loop.
n=int(input("enter the number :"))
fac=1
if n==0:
    fac=1
else:
    for i in range(1,n+1):
        fac=i*fac
print(f"The Factorial of the number {n} is",fac) 