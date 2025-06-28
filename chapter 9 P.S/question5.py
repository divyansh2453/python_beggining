# 5. Repeat program 4 for a list of such words to be censored.
with open("paragraph.txt") as f:
    line=f.read()
f.close()

line=line.replace("Donkey","######")
line=line.replace("donkey","######")
line=str(line)

with open("paragraph.txt", "w") as g:
    g.write(line)
    print("edited the file")
