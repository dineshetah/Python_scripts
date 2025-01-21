#Functions with inputs Arguments& Parametes

def my_function():
    Do this 
    Then do this 
    Finally do this.
#Review:
#create a function called greet().
#Write 3 print statements inside the function
#call  the greet() function and run your code.

def warmwelcome():
    print("Hello ")
    print("How are you ?")
    print("Fine and you ?")
warmwelcome()

#functions with inputs 
def my_function(something):
    Do this        # inside this do some thing
    Then do this 
    finally do this 

def warmwelcome_name(name):
   
    print("Hello",name)
    print(f"How are you ?")
   
warmwelcome_name("DINESH")

# something    = 123
#    |            |
# parameters      Argument actual values 

#Positional vs. keyword Arguments 

def warmwelcome_with(name, location):
    print(f"Hello {name}" )
    print(f"What is it like in {location}")
warmwelcome_with("Dinesh", "Delhi")

positional Arguments
def my_functions(a,b,c):
    do this with a            a = 1
    then do this with b       b = 2 
    finally do this with c    c = 3

#Keyword Arguments
def my_functions(a,b,c):
    do this with a          
    then do this with b 
    finally do this with c  

# functions with keyword arguments
#warmwelcome_with(location="london",name="Dinesh")

#you are painting a wall.The instructions on the point can says that 1 can of point can cover 
# 5 square meters of wall. Given a random height and width of wall, calculate how many cans of point you'll need to day 

formula = (wall height * wall width)+ coverage per can 

import math
def calculation_paint(height,width,coverage): # creating function 
    number_cans =(height*width)/coverage
    round_up_cans = math.ceil(number_cans)
    print(f"you will need {round_up_cans} cans of point")
height_new= int(input())
width_new = int(input())
coverage= 5
calculation_paint(height=height_new, width=width_new, coverage=5) # calling function

# check wheater number prime or not 

def prime_num(number):
    is_prime = True
    for i in range (2,number):
     if number % i ==0:
            is_prime =False
    if is_prime :
     print("It is a prime number.")
    else:
       print("It is not prime number.")
user_input = int(input("Enter a number: "))
prime_num(number=user_input)

# another way check prime number 

def prime_num():
    number = int(input("Enter a number: "))
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break  # Optimize by breaking the loop if a divisor is found

    if is_prime and number > 1:  # 1 is not a prime number
        print("It is a prime number.")
    else:
        print("It is not a prime number.")

prime_num()  # Call the function without passing any arguments



# for caesar related code 

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # single line store alphabets 

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") # input fields 
text= input("Type your message:\n").lower() #input fields 
shift = int(input("Type the shift number:\n")) #input fields

#Todo-1:- create a function called 'decrypt' taht takes the text and 'shift as inputs 
def encrypt_model(plain_text,shift_amount):
   
#Todo-2:- Inside the 'encrypt'function, shift each letter of the 'text
# forwards in the alphabet by the shift amount and print the encrpty text.
   
   cipher_text = " "
   for letter in plain_text:
    position = alphabet.index(letter)
    new_position=position + shift_amount
    new_letter  = alphabet[new_position]
    cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")


#Todo-3:- Call the encrypt function and pass in the user inputs.You should be able to test the code and encrypt a message.
#encrypt_model(plain_text=text,shift_amount=shift)


# for caesar related code 

# Todo-1:- create a function called 'decrypt' taht takes the text and 'shift as inputs 
def decrypt_model(cipher_text,shift_amount):
  
# Todo-2:- Inside the 'encrypt'function, shift each letter of the 'text
# **backwards** in the alphabet by the shift amount and print the decrptyed text.
  
    plain_text = " "
    for letter in cipher_text:
      position = alphabet.index(letter)
      new_position=position - shift_amount
      plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")
    decrypt_model(cipher_text=text,shift_amount=shift)

# Todo-3:- check if the user wanted to encrypt or decrypt the message by checking the 'direction
# variable. Then call the correct function based on that 'direction' variable.You should be able to test the code to encrpy and decrypt a message.
encrypt_model(plain_text=text,shift_amount=shift)
    
if direction == "encode":
      encrypt_model(plain_text=text,shift_amount=shift)
elif direction == "decode":
      decrypt_model(cipher_text=text,shift_amount=shift)


#TODO1-: combine the encrypt() and decrypt() function into a single function called ceasar()
def ceasar(start_text, shift_amount, cipher_direction):
   end_text = ""
   if cipher_direction == "decode":
      shift_amount*=-1
   for letter in start_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
   print(f"Here's the {direction}d result:{end_text}")
      
#ToDO-2: call the ceasar () function, passing over the 'text','shift' and 'direction' values.
ceasar(start_text=text,shift_amount=shift,cipher_direction=direction)

#TODo-1: import and print the logo from logo.py when the program starts.
from drwing_logo import logo
print(logo)

def caesar(starti_text, shift_amount, cipher_direction):
   end_text =""
   if cipher_direction == "decode":
      shift_amount *= -1
      for char in starti_text:
         if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text +=alphabet[new_position]
         else:
            end_text += char

#TOdo-4:- Can you figure out a way to ask the user if they want to restart the
# cipher program ?
#e.g Type 'yes if you want to go again. Otherwise type'no'.
#if they type 'yes' then ask them for the direction/text/shift again and 
#call the ceasar() function again ? 
#Hint: Try creating a new function that calls itself if they they type 'yes'
should_continue =True
while should_continue:
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
   direction = input("Type your message:\n")
   direction = input("Type the shift number:\n")

#Todo-2:- what if the user enters a shift that is greater than the number of letters
# in the alphabet?
#Try running the program and entering a shift numbers of 45.
#Hint:Think about how you can use the modulus(%).
shift = shift % 26 
caesar(start_text =text, shift_amount =shift, cipher_direction = direction )
result =input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if result == "no":
   should_continue =False
   print("Good Bye")
