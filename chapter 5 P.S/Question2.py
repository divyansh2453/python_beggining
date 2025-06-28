# Write a program to input eight numbers from the user and display all the unique
# numbers (once).
s=[]
print('enter eight number to print unique ones')
for i in range(1,9):
    num=int(input(f"enter the {i} number :"))
    s.append(num)
print("here are the result:")    
sn=set(s)
print(sn)