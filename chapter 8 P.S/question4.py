# 4. Write a recursive function to calculate the sum of first n natural numbers.
num=int(input("enter a number :"))
def sumn(num):
    if num==1:
       return 1
    return sum(num-1)+num

print("the sum of first n natural number is :",sumn(num))