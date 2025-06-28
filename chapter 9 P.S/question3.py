import os

# Create a folder for the files
folder_name = "tables_for_13_year_old"
os.makedirs(folder_name, exist_ok=True)

# Generate multiplication tables from 2 to 20
for i in range(2, 21):
    filename = os.path.join(folder_name, f"{i}.txt")
    with open(filename, "w") as g:
        for j in range(1, 11):
            g.write(f"{i} X {j} = {i * j}\n")