# Write a program to find out whether a given post is talking about “Harry” or not.
post=input("enter the post")
if post.find("harry")!= -1 or post.find("Harry")!= -1:
    print("the post is talking about harry")
else:
    print(" the post is NOT talking about harry")
    