## Errors, Exceptions and Saving JSON Data

## FileNotFound 
# with open("a_file.txt") as file:
#     file.read()

## KeyError
# a_dictionary = {"key":"value"}
# value =a_dictionary["non_existent_key"]

## IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

##TypeError
# text = "abc"
# print(text + 5)

# Remember: try:, except:, else, finally: these are four keywords when it come to handing error or expections 


# try:
#     file = open("a_file.txt")  # if there is not file path
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"]) # Here this is not actually key
# except FileNotFoundError:
#     #print("There was an error !")  # then print inside the text here 
#     file =open("a_file.txt", "w")  # New file created a_file1
#     file.write("Something")
# # except KeyError:
# #     print("That key does not exist.") #so here print same line of message 

# except KeyError as error_message:
#     print(f"That key{error_message} does not exist.") #so here f string with key value for same line of messag

# else:
#     content = file.read()
#     print(content)

# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError #KeyError

#------------Raising your own Exceptions-------------------------

# height = float(input("Height:"))
# weight = int(input("Weight: "))

# if height > 3 : 
#     raise ValueError("Human Height should not be over 3 meters.")
# # Here, WE will show error value error invalid bmi calculate 
# bmi = weight/height*2
# print(bmi)

# Auditorium question solution 

#TODO: Catch the exception and make sure the code runs with  

# OBJECTIVE : Use what you have learnt about exceptions handling to prevent the program
# from crashing. If the user enters somethings that out of range just print a 
# default output of "Fruit pie".

# fruits = eval(input())  # convert formatted sting to list 
# Catch the exceptions and make sure the code runs without crashing.
# def make_pie(index): # Here it is except an index arguement 
#     try:
#         fruit =fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + "Pie")
# make_pie(4)


# We have got some buggy code, try running the code. The code will crash and

# facebooks_posts =eval(input("Enter the your choice ?"))
# total_like = 0
# for post in facebooks_posts:
#     try:
#         total_likes = total_like + post['Likes']

#     except KeyError:
#         pass
# print(total_likes)



## Exception Handilling in the NATO Phonetic Alphabet Project
import pandas

data = pandas.read_csv("C:\\Users\\KIIT\\Desktop\\100Days_code_programming\\nato_phonetic_alphabet.csv")
def generate_phonetic():
    phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
    print(phonetic_dict)
    word =input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic() # here after handling error then again ask for enter correct input 
    else:
        print(output_list) 
generate_phonetic()



# So, here actually needed these all thing should be looping so def generate_phonetic()

# Write, read and update JSON data in the Password Manager 
# JSON means JavaScriptObjectNotation 
