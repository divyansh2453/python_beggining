# 7. Write a program to find out the line number where python is present from ques 6.
lno=1
location=[]
with open("log.txt") as f:
    line=f.readline()
    while line != "":
        line=f.readline()
        # print(line)
        line=line.lower()
        if line.find("python")!=-1:   
            location.append(lno)
            print(line)
            lno+=1

print("The word Python was found in :",location)
            