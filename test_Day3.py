#control flow with if/else main scenarios 
# if condition:
#   do this 
# else:
#   do this


#Exmple a water level for above scenarios 
# water_level = 50 
# if water_level >80:
#     print("Drain water")
# else:
#     print("Continue")


# Example for the person height valid or not for the drive conditions 
#Person_height =120
# Person_height = int(input("Enter the person height"))
# if Person_height>=120:
#     print("You can elligble for drive!")
# else:
#     print("You can't elligble for drive!")

# comparison Operators in python 
    # >      greater than 
    # <      less than  
    # >= Greater than or equal to 
    # <= less than or equal to 
    # == equal to 
    # != not equal to
    
#Auditorium questions
# number = int(input())
# if number %2==0:
#     print("Even number")
# else:
#     print("Odd number")

#Nested if statement and elif statements main scenarios with example 
# if condition:
#     if another condition:
#       do this
#     else:
#         do this 
# else:
#     do this

# Person_height = int(input("Enter the person height"))
# if Person_height>=120:
#     print("You can elligble for drive!")
#     age = int(input("what is your age?"))
#     if age<=18:
#         print("Please pay Rs. 10")
#     else:
#          print("Please pay Rs. 15") # from if to print these are under condition nested loop
# else:
#     print("You can't elligble for drive!")

# Use of if/elif/else main scenarios for these conditions with example 
# if condition1:1
#    do A
# else:
#   do this 

# if condition1:1
#    do A
# elif condition2:
#    do B
# else:
#   do this 


# Person_height = int(input("Enter the person height"))
# if Person_height>=120:
#     print("You can elligble for drive!")
#     age = int(input("what is your age?"))
#     if age<12:
#         print("Please pay Rs. 5")
#     elif age<=18:
#         print("Please pay Rs. 10")
#     else:
#          print("Please pay Rs. 15") # from if to print these are under elif condition use many times 
# else:
#     print("You can't elligble for drive!")

# Calculate EMI fourmala for specific conditions
    
# height = float(input())
# weight = int(input())
# bmi_formula = weight/height*height
# if bmi_formula<18.5:
#     print("Your BMI is {bmi_formula}, you are underweight.")
# elif bmi_formula <25:
#     print("Your BMI is {bmi_formula}, you have a normal weight.")
# elif bmi_formula<30:
#     print("Your BMI is {bmi_formula}, you are slightly weight.")
# elif bmi_formula<30:
#     print("Your BMI is {bmi_formula}, you are obese.")
# else:
#     print("Your BMI is {bmi_formula}, you are clinically obese.")

# Another example for leap year or non leap year
# year = int(input())
# if year% 4==0:
#     if year% 100== 0:
#       if year% 400==0:
#         print("This is a leap year")
#       else:
#           print("Not Lear year")
#     else:
#         print("Leap Year")
# else:
#     print("Not Lear year")

#multiple if/elif/else statements in succession main scenarios and with example
# if condition1:                               | if condition1:
#     do A                                         do A
# elif condition2:                               if condition2:
#     do B                                         do B
# else:                                          if condition3:
#     do C                                         do C

# Person_height = int(input("Enter the person height"))
# if Person_height>=120:
#     print("You can elligble for drive!")
#     age = int(input("what is your age?"))
#     if age<12:
#        bill = 5 
#        print("Child tickets are Rs.50")
#     elif age<=18:
#         bill = 7
#         print("Youth tickets are Rs.100")
#     else:
#          print("Adult tickets are Rs.200") # from if to print these are under elif condition use many times 
# wants_photo =input("Do you want a photo taken ? Y or N. ")
# if wants_photo == "Y":
#     bill+= 50              
#     print(f"Your final bill is {bill}")
# else:
#     print("You can't elligble for drive!")

# Auditorium Problem solution, pizza order with interactive coding 

# print("Thank you for choosing python pizza deliveries!")
# size = input() #what size pizza as S,M,or L 
# add_pepperoni = input() # do you want ? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# bill = 0 
# if size =="S":
#     bill+=15
# elif size == "M":
#     bill+= 20
# else:
#     bill +=25
# if add_pepperoni =="Y":
#     if size =="S":
#         bill +=2
#     else:
#         bill +=3
# if extra_cheese =="Y":
#     bill +=1
# print(f"Your final bill is:{bill}.")

# Auditorium problem solutions 
#The love calculator is calculating your score,,,
print("The love calculator is calculating your score...")
name1 = input()
name2 = input()
combined_name = name1 +name2
lower_name = combined_name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

first_digit  = t+r+u+e 
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

second_digit = l+o+v+e
score = first_digit + seecond_digit
if (score<10) or (score>90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40) and (score<=50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"your score is {score}")
