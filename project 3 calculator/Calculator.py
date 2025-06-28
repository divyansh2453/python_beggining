again=True
print("     CALCULATOR        ")
while(again==True):
    n1=int(input("Enter the First Number  :"))
    n2=int(input("Enter the Second Number :"))
    print(" ")
    print(" Enter the Operator ")
    print("1. Multiplication\n2. Addtion\n3. Substraction\n4. Division")
    oper=int(input("enter the Number of Operator :"))
    if(oper==1):
        print(n1, "X", n2, "=" ,n1*n2)
    elif(oper==2):
        print(n1, "+", n2, "=" ,n1+n2)
    elif(oper==3):
        print(n1, "-", n2, "=" ,n1-n2)
    elif(oper==4):
        print(n1, "÷", n2, "=" ,n1/n2)
    else:
        print("wrong operator")
        exit
    again=bool(input("Wanna Do Another Calculation : True/False"))
