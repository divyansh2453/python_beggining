# 8. If languages of two friends are same; what will happen to the program in problem
# 6?
s={}
for n in range(0,4):
    nm=input("enter your name : ")
    ln=input("enter your language : ")
    s.update({nm:ln})  
print(s)
print("nothing extra happens")
