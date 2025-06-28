# Write a program to sum a list with 4 numbers.
num=[]
for i in range(0,4):
    number=int(input("enter number to find the sum :"))
    num.append(number)
summ=sum(num)
print(summ)
