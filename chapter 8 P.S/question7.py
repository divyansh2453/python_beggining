# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.
l=[]
for i in range(0,5):
    nm=input("enter the name :")
    l.append(nm)
# l=["divyansh", "Dev", "Shubham", "am"]
def rem(l, word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n        

n=rem(l, "am")
print(n)
