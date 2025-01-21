#How can password generator,

#How to generate strong passwords with letters and symbols and numbers. First, how many letters would you like in your password?

#I would like 12. How many symbols would you like? I would like 2.
# Here is like password: hHkCC&0uKlFu2b#$%7G

# Using the for loop with Python Lists 

state_name = ["Uttar Pradesh","Bihar","Meerut","Delhi"]
for state in state_name:
    print(state)
    print(state +" "+"Bihar")
    print(state_name)

# calculate the highest score from a lists of score 
# eg. students_scores = [78,65,89,55,91,64,89]

stu_score = input().split()
for m in range(0,len(stu_score)):
    stu_score[m]=int(stu_score[m])

h_score = 0
for s in stu_score:
    if s> h_score:
        h_score =s
        #print(h_score)
print(f"The highest score in this class is :{h_score}")

For loop with Range 
for number in range(1,10):       # range (1,10) get 1-9 only why 
    print(number)

for number in range(1,11):       # range (1,11) get 1-10 why increase one
    print(number)

for number in range(1,11,3):     # range (1,11,3) get 1,4,7 why step by 3 
    print(number)

total = 0
for number in range (1, 101):
    total += number
    print(number)

#write a program that calculate the sum of all the even number from 1 to X.
#If X is 100 then first even number wouble be 2 and last one is 100

target =int(input())  # number between 0 and 1000
even_sum = 0 
even_sum +=number
for number in range(2,target+1,2):
    even_sum += number
print(even_sum)

alt_sum = 0
for number in range(1,target+1):
    if number%2 ==0:
        alt_sum += number 
print(alt_sum)

print(number)

printing first 6 whole number

for i in range(6):
    print(i, end=" ")
print()
#write a program to recreate the FIZZBuzz game 

target = 100
for number in range(1, target+1):
     if number % 3 == 0 and number % 5 == 0:
         print("FuzzBuzz")
     elif number % 3 == 0:
         print("Fizz")
     elif number % 5 == 0:
         print("Buzz")
     else:
         print(number)

## password Generator project
         
import random
letter  =['a','b','c','d','e','f','g','h','i','k','l','A','B','C','D','E','F','G','H','I','K','L']
number = ['0','1','3','4','5','6','7','8','9']
symbols = ['!','@','#','%']
print("Welcome to the PyPassword Generator!")
Eng_letters=int(input("How many letter would like in your password"))
special_symobols  =int(input(f"How many symbols would you like?\n"))
digit  =int(input(f"How many number would you like?\n"))
password = ""
for char in range (1,Eng_letters+1):
    random_char = random.choice(Eng_letters)  # random.choice function
    print(random_char)


###################################
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L']
numbers = ['0', '1', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '%']

print("Welcome to the PyPassword Generator!")

Eng_letters = int(input("How many letters would you like in your password? "))
special_symbols = int(input("How many symbols would you like? "))
digits = int(input("How many numbers would you like? "))

password_list = []

# Generate random letters
for _ in range(Eng_letters):
    password_list.append(random.choice(letters))

# Generate random symbols
for _ in range(special_symbols):
    password_list.append(random.choice(symbols))

# Generate random numbers
for _ in range(digits):
    password_list.append(random.choice(numbers))

# Shuffle the generated password characters
random.shuffle(password_list)              #call random.shuffle(some_list), it will shuffle the elements of some_list into a new random order. 

# Convert the password characters list to a string
password = ''.join(password_list)

print("Your generated password is:", password)
