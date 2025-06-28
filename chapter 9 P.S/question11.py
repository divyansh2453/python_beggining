# 11. Write a python program to rename a file to “renamed_by_ python.txt.
with open("oldone.txt") as f:
    t=f.read()
with open("renamed_by_ python.txt", "w") as g:
    g.write(t)
        