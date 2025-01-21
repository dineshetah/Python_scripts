# Day 26 List Comprehension 
# For Loop 
number = [1,2,3,4]
new_list = []
for n in number:
    add_1 = n + 1 
    new_list.append(add_1)
print(new_list)

# List Comprehension 

new_list = [new_item for item in list ]

new_list = [n+1 for n in number]
print(new_list)

name = "Dinesh"
letters_list = [letter for letter in name]
print(letters_list)

# Here I mentioned python Sequences 
#list, range, string, tuple

# range(1, 5) [2,4,6,8]

num = [1,2,3,4]
new_number = [num*3 for num in range(1, 5)]
print (new_number)  # Here, {list:4} output [2,4,6,8] with list 

# Conditional list comprehension 
new_list = [new_item for item in list if test]  # writting trick 

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [new_item for item in list if test] using this concept 
short_names = [name.lower() for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(long_names)

# Auditorium solution 
numbers = [1, 1 , 2, 3, 5 ,8 , 9, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)

# In this list comprehension exercise for practise using list comprehensive 
# to filter out the even numbers from a series of numbers 

list_of_strings  = input("Enter the any number ?").split(', ') # here split use separate comma and space  
numbers = [int(x) for x in list_of_strings]

Even_number = [num for num in number if num % 2 == 0]
print(Even_number)


# Here take a look inside file1.txt and file2.txt.They each contain a 
# bunch of numbers each number on a new line.

# You are going to create a list called result which contains the numbers that are common in both file 

# HINT . USe the keyword method for starting the list comprehensive and fill in the relevant parts 
## First we will need to read from the files and create a list using the lines in the files 
## check https://www.w3schools.com/python/ref_file_readlines.asp
## check https://www.w3schools.com/python/python_ref_keywords.asp

with open("C:\\Users\\KIIT\\Desktop\\100Days_code_programming\\file1.txt", "r") as file1:
  list1 = file1.readlines()  # Here we get a list1 with readlines method that contain numbers

with open("C:\\Users\\KIIT\\Desktop\\100Days_code_programming\\file2.txt", "r") as file2: # Here we get a list2 that contain numbers
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]
print(result)

# How to use Dictionary Comprehension 

new_dict = {new_key : new_value for item in list}
new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random
students_scores = {new_key:new_value for item in names}
students_scores = {new_key:new_value for student in names}
students_scores = {student:random.randint(1, 100) for student in names}

print(students_scores) # this is for print out the random score 

students_scores = {"Alex" : 55 , "Caroline": 60}

passed_students = {new_key:new_values for(key, value) in dictionary.items()} # here the key, value call the item method for dictionary

passed_students = {student:score for(student, score) in students_scores.items() if score >= 50}  # here if condition there for score is greater than 

print(passed_students)

# auditorium problem solution 
#TODO: Write a code use dictionary comprehensive to create a dictionary call result 
# that takes each word in the given sentences and calculates the number of letter 
#in each word.

string = 'This is a string ,,with words!'
print(string.split())

sentence = input()
result ={word:len(word) for word in sentence.split()} # here is key:value  
print(result)

# Another auditorium problem 
# Here, we are going to use dictionary comprehensive to create a dicitionary called 
# degrees Fahrenheit.

# To convert temp_c in temp_f use this formula:

temp*9/5 + 32 = temp_f

# Here eval() converts correctly formatted string to dict 

weather_c = eval(input("Enter a temperature in Celsius: "))
#Dictionary comprehensive 
weather_f = {day:temp for (day,temp)in weather_c.items()}
weather_c_input = input(("Enter a temperature in Celsius: "))
weather_c = eval(weather_c_input)
weather_f = {day:temp*9/5 + 32 for day,temp in weather_c.items()}
#print(weather_c)

# How to Iterate over a Pandas DataFrame 

student_dict  = {
    "student" : ['Angela', 'James', 'Lily'],
    "score" : [56, 76, 98]
}
# Using for looping through student_dict 
for (key, value) in student_dict.items():
  Access key and value 
    print(key) 
    print(value)
#Here print out the result studen, key  

import pandas 
student_df =pandas.DataFrame(student_dict)
print(student_df) 

# Looping through a data frame 
for (key, value) in student_df.items():
    print(value)

# Looping through rows of a data frame 
for (index, row) in student_df.iterrows():
   # access the index and row 
   print(row.student) # here print out each of the student record inside data frame 
   print(row.score)
   # Access row.student and row.score  
   if row.student == "Angela":
       print(row.score)

# Introducing the NATO Alphabet Project 
    
{key:value for (index, row) in df.iterrows()}
       
      
    df = pandas.read_csv("C:\\Users\\KIIT\\Desktop\\100Days_code_programming\\nato_phonetic_alphabet.csv")
print(df)
print(df.to_dict())
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs 
word = input("Enter the word? ").upper()
# Looping inside the list 
# [new_item for item in list] basis of the formate 
phoetic_list = [phonetic_dict[Letter] for Letter in word]
# Here, access the dictionary to list
print(phoetic_list)