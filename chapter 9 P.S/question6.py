# 6. Write a program to mine a log file and find out whether it contains ‘python’.
with open("log.txt" ,"r") as f:
    tmp=f.read()
    tmp=tmp.lower()
      
if (tmp.find("python")==-1):
    print("Python Not Found !")

elif (tmp.find("python")!=-1):
    print("Python Found !")

else:
    print("Not Working !!")  