################## Scope #################################
# enemies  = 1 

# def increase_enemies():
#     enemies = 2 
#     print(f"enemies inside function :{enemies}")    # if run this function, not be get any output 
# increase_enemies()

# print(f"enemies outside function :{enemies}")


######### Local Scope #################

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# drink_potion                # if run this function, not be get any result 
# print(potion_strength )     # will get error 



############  Global Scope ########################
# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)   # after run this print function, not be get any result 
# drink_potion()             # then will get output 10

# Note: This concept of global and local scope does not apply to variable .

# Does Python have block scope ?

# There is no Block Scope 
game_level = 3
enemies = ["Skeleton","Zombie","Alien"]
if game_level<5:
    new_enemy = enemies[0]
print(new_enemy)      # this print function used to inside if loop condition 



# How to modify variable with Global Scope

# enemies  = 1

# def increase_enemies():
#     global enemies      
#     enemies = +1
#     print(f"enemies inside function :{enemies}")    # if run this function, not be get any output 
# increase_enemies()

# print(f"enemies outside function :{enemies}")

# Global Constants
pi = 3.14159
URL ="isbtsoulunileaders.com"
TWITTER_HANDLE = "@DINESH1223"

def calc():
    TWITTER_HANDLE
calc()   # nothing will get as output 
print(pi)
#Question 1: What will be printed in the console when the following code is run? DO NOT run the code, just pretend to be a computer.

# def a_function(a_parameter):
#     a_variable = 15
#     return a_parameter
 
# a_function(10)
# print(a_variable)      #output will be give error Name error 

#Question 2:What will be printed in the console when the code is run? DO NOT run the code, just pretend to be a computer.

i = 50
def foo():
    i = 100
    return i
 
foo()
#print(i)  # this print function will be execute only outside define variable mean global variable 

# Question 3:What will be printed in the console when the following code is run?DO NOT run the code, just pretend to be a computer.

def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()

###################################################

import random 
from random import randint 

EASY_LEVEL_TURNS  =10            # THIS IS TWO GLOBAL VARIABLE  ASSIGNED
HARD_LEVEL_TURNS = 5             

# Function to check user's guess against actual answer.
def check_answer(guess, answer):
    if guess_number>answer:
        print("Too High")
    elif guess < answer:
        print("Too Low")
    else:
        print(f"You got it! The answer was {answer}.")

#Repeat the guessing functionality if they get it wrong.
#while
# Make function to set difficulty 
def set_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard': ")
    if level == "easy":  # now then it is time create this global 
        #turns =EASY_LEVEL_TURNS
        return EASY_LEVEL_TURNS            # then it can simple calll this function set_difficulty
        global turns # here it is not valid global 
    else:
        #turns =HARD_LEVEL_TURNS
         return HARD_LEVEL_TURNS
def game():
# Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a Number 1 and 100")
    answer  = randint(1, 100)
    print(f"Pssst,the correct answer is {answer}")
    turns = set_difficulty
    print(f"You have {turns} 5 attempts remaining to guess the number.")
    # Let the user guess a number.
    guess_number = 0
    while guess_number !=answer:
     guess_number = int(input("User is making guess:"))
    check_answer(guess_number,answer)
game()
#turns = 0
#turns = set_difficulty
#print(f"You have {turns} 5 attempts remaining to guess the number.")
#Track the number of turns and reduce by 1 if they get it wrong.

#Repeat the guessing functionality if they get it wrong.

