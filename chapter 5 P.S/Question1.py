# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
meaning={"car":"vahan","book":"pustak","pot":"gamla"}
print("hello user")
print(f"this program allows u to see a list of word in english \nand check there english transaltion")
print(meaning.keys())
opt=input("enter the word u want to translate :")
print(meaning.get(opt))
