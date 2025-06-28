# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
math=int(input("enter marks in math:"))
eng=int(input("enter marks in english:"))
science=int(input("enter marks in science:"))
per=(str((math+eng+science)*(100/300))+("%"))
cent=(math+eng+science)*(100/300)
print("your overall percentage is :",per)
status=False
if math>33:
    if eng>33:
        if science>33:
           print("you have more than 33% in each subject")
           status=True
        else:
            print("u have failed in Sciece") 
            breakpoint   
    else:
        print("u have failed in English")
        breakpoint
else:
    print("u have failed in Math")        
breakpoint
if status==True and cent>=33:
    print("u have passed the exam")