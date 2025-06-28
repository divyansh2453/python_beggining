# If the names of 2 friends are same; what will happen to the program in problem
# 6?
s={}
for n in range(0,4):
    nm=input("enter your name : ")
    ln=input("enter your language : ")
    s.update({nm:ln})
opt=input("whose fav lang u want to see :")    
print(f"the fav subject of {opt} is ",s.get(opt))
print(s)
print("the new data will be accepted if the same key is used twice")
