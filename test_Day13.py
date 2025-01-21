# Debugging 
# In this Day13 some techniques and tips for how to find bugs and how get rid of them in our code
# Grace Hopper lady first documented bug actually found 
# Step -1: Describe the problem 
# the problem is messy and it is not well understood in mind
# then impossiable to debug 
# if in your code commented first removed all commented portion 

""" 
we're going to practice describing the problem to help us solve this debugging problem. Now if you take a look at this function

you can see that at some point in the function, we're supposed to print this line out into the console.
"""
# Describe Problem 
def my_function():
    for i in range (1,20):        # range will always keep in mind  last +1
        if i ==19:
         print(f"you got it:")   # Nothing will be printing 
my_function()   # Also nothing will be printing after remove commet then run will gets print  

# What is the for-loop doing? When is the function meant to print "You got it"?
# Answer : range (start, end)

# Reproduce the bug 
from random import randint
dice_imags = ["1","2","3","4","5","6"]
dice_num = randint(1,5)
print (dice_imags[dice_num])  # we are getting error list index out of range

# Play Computer 
year = int(input("What is your year of birth?"))
if year > 1980 and year < 1994:
    print("Your are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")
# In this above code if you are entering 1994 nothing will not be get output. So use year=< 1994 
    
# Fix the Error 
age = int(input("How old are you ? "))    # use int datatype for string error 
if  age > 18:
 print("You can drive at age {age}.")

# # Print is your friend 
pages = 0   # doen't meaning 
word_per_pages  = 0     # doen't meaning 
pages = int(input("Number of words per pages: "))
word_per_page = int(input("Number of word per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")                     # Remember printing things fstring 
print(f"word_per_page = {word_per_page}")
print(total_words)


# Another way same code writting 
pages = int(input("Number of pages: "))
word_per_pages = int(input("Number of words per page: "))

total_words = pages * word_per_pages
print("Total words:", total_words)

# Use a Debugger 
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)
# This code use for debugging FizzBuzz
    
target = int(input())                #error string use with int 
for number in range(1, target+1):
     if number % 3 == 0 and number % 5 == 0:
         print("FuzzBuzz")
     elif number % 3 == 0:     # use elif not if 
         print("Fizz")
     elif number % 5 == 0:
         print("Buzz")
     else:
         print(number)

# Debugging for even or odd num 
import math
num = int(input("Enter the number: "))
                   # not menstioned int data type 
if num % 2 == 0:          # use single = symbol that 
    print(f"Number Even : {num} ")
else:
    print(f"Number Odd: {num} ")


"""     
#1.Check Syntax Errors: Ensure there are no syntax errors in your code. 
Python's interpreter will throw errors if there are syntax issues, so fixing them is a crucial initial step.

#2.Use Print Statements: Place print statements strategically throughout your code to display the values of variables, 
especially before and after crucial operations, to track their values.

#3.Logging: Utilize Python's logging module to create logs with different levels of severity 
(e.g., debug, info, warning, error, critical). It allows you to have more control over the output and enables logging in production.

#4.Debugger (pdb): Employ Python's built-in debugger pdb to set breakpoints, 
inspect variables, and step through your code to analyze its execution flow.

#5.Exception Handling: Implement try-except blocks to catch and handle exceptions gracefully. 
This helps in preventing crashes and provides insights into what went wrong.

#6.Code Reviews: Engage peers or colleagues for code reviews. 
Fresh perspectives often catch errors or potential issues that you might have missed.

#7.Unit Testing: Create unit tests for your code using Python's 
unittest or other testing frameworks like pytest to validate individual units of your code.

#8.Static Analysis Tools: Leverage tools like flake8, pylint, or mypy to perform static code analysis. 
These tools can identify potential issues, enforce coding standards, and catch errors.

#9.Isolate Problematic Code: If debugging complex code, isolate the problematic part into smaller, testable sections. 
This way, you can focus on specific areas rather than the entire codebase.

#10.Documentation and Comments: Maintain good code documentation and comments. Sometimes, 
just explaining your code in detail can help you spot mistakes or oversights.

"""