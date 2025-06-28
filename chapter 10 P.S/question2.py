# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.
class calc():
    def __init__(self,num):
        self.num=int(num)

    def square(num):
        print(f"the square of {num} is",num**2)
    
    def cube(num):
        print(f"the cube of {num} is",num**3)
    
    def root(num):
        print(f"the root of {num} is",num**0.5)

num=int(input("enter a number :"))

calc(num)

print('''what u want to do
1.square
2.cube      
3.square root
''')

opt=int(input("enter your option:"))

if opt==1:
    calc.square(num)
elif opt==2:
    calc.cube(num)
elif opt==3:
    calc.root(num)    