# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
with open("poems.txt") as f:
    text=f.read()
    if not(text.find("twinkle")==-1):
        print("found")
    else:
        print("not found")

