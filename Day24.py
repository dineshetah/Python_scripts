# Day24 use Python to open up files read files write to the files without touching the mouse 

# file = open("24daytext.txt")
# context = file.read()
# print(context)

# Also another way 

# with open("24daytext.txt") as file:  # with keywords directly file managed 
#    context = file.read()
#    print(context)


# with open("24daytext.txt") as file:
#    file.write("new add title yadav.")       # Here, we are getting unsupportedOperation not writable
# 
# with open("24daytext.txt",mode="w") as file:  # Here, define mode with w mean write then successfully executed 
#    file.write("new add title yadav.")    # and check text file previous text is deleted replace new txt after exection 
# 

# with open("24daytext.txt",mode="a") as file:  # Here only change mode with a means append anything with \n new line 
#    file.write("\nAdd new title.")

# with open("24day_dummytext.txt",mode="w") as file: # Here change new txt file with mode a-append & w- write mode only 
#    file.write("Add new title.")
# 
# a = 3
# print(a)
# a = input("what do you want a to equal?: ")
# print(a)

# Here we have managed to get the snake game to keep track of the high score
# Here we replace that high score with the new value. 
# first of all the create new text file with containing a single number 

# TODO: create a letter using starting_letter.txt
# for each name in invited_name.txt.
# Replace the [name] placeholder with actual name.
# save the letters in the folder"ReadyToSend"

# Hint1: this will help you
# https://www.w3schools.com/python/ref_string_replace.asp 
# Hint2: this will help you
#https://www.w3schools.com/python/ref_string_readline.asp

# Hint3: this will help you
#https://www.w3schools.com/python/ref_string_strip.asp

# txt = "banana "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")

# # Remove the leading and tailing character:

# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)



with open("./Input/Names/invited_name.txt") as names_file:
    names = names_file.read()
print(names)