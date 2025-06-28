# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3
i=0
st=1
n=int(input("enter the number :"))
base=st+(2*n)
while(i<n):
    patt="*"*st
    print(patt.center(base))
    st+=2
    i+=1