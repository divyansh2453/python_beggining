# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
com=input("enter the comment :")
if (com.find("Make a lot of money")!=-1 or com.find("buy now")!=-1 or com.find("suscribe this")!=-1 or com.find("click this")!=-1 ):
   print(" this is a spam comment.")
else:
   print("this comment is not a spam")
   
