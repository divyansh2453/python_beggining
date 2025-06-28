# 9. Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * *
n=int(input("enter the number :"))
sp=(" "*(n-3))
border=("*"*n)
print(border)
cen="*"+ sp +"*".center(n)
for i in range (1,n-1):
    print(cen)
print(border)