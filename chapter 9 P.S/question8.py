# 8. Write a program to make a copy of a text file “this. txt”
with open("this.txt") as f:
    txt=f.read()

with open("thiscopy.txt", "w") as g:
    g.write(txt)
    