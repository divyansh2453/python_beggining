# 2. Write a python program using function to convert Celsius to Fahrenheit.
#  F = (C * 9/5) + 32
num=int(input("enter a temperature in Celsius :"))
def ctof(c):
    fe=((c*9/5)+32)
    print(f"the temperature in farenheit is :{fe}")
          
ctof(num)

