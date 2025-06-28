# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique
s={}
for n in range(0,4):
    nm=input("enter your name : ")
    ln=input("enter your language : ")
    s.update({nm:ln})
opt=input("whose fav lang u want to see :")    
print(f"the fav subject of {opt} is ",s.get(opt))
