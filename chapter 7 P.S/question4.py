# 4. Write a program to find whether a given number is prime or not.
n=int(input("enter a number : "))
m=0
for i in range(1,n):
    if n%i==0:
        m+=1

if (m>1):
    print("This is not a Prime Number")  
else:
    print("This is a Prime Number")