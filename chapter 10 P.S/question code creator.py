lst=[]
for i in range(1,7):
    lst.append(f"question{i}"+".py")
print(lst)    
for item in lst:
    with open(item, "w") as g:
        g.write("")
         