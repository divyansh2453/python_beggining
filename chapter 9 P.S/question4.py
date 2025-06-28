# 4. A file contains a word “Donkey” multiple times. You need to write a program
#    which replace this word with ##### by updating the same file.
with open("paragraph.txt") as f:
    line=f.read()
f.close()

line=line.replace("Donkey","######")
line=line.replace("donkey","######")
line=str(line)

with open("paragraph.txt", "w") as g:
    g.write(line)
    print("edited the file")
