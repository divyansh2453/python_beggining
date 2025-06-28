# 9. Write a program to find out whether a file is identical & matches the content of
# another file.
name1=input("enter the name of file 1:")
name2=input("enter the name of file 2:")

with open(name1) as f:
    f1=f.read()

with open(name2) as g:
    f2=g.read()

if (f1==f2):
    print("The files are Identical !!!!")
else:
    print("The files are diffrent !")