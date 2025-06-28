# 8. Write a python function to print multiplication table of a given number.
num=int(input("enter a number for multiplication :"))
def mult(n):
    for i in range(1,11):
        print(f"{n} X {i} =",i*n)
    return "done"        

mult(num)