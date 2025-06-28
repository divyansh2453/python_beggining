# 10. Write a program to wipe out the content of a file using python.
name1=input("enter the name of file :")
name=name1+".txt"
with open(name) as f:
    data=f.read()

if (data==""):
    print("File is already empty")
elif(data!=""):
    with open(name, "w") as g:
        g.write("")
        print("Data Cleared !!")    
else:
    print("something went wrong")