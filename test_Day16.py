## OPP -  Object Oriented Programming 
## In this DAY16 some of the coding cases what is going on with my code?
## so feel to like our code is getting more complex. It's try to do a lot of thingss
## To manage a whole bunch of relationships one function is changing a variable, do something else change 
## another variable etc. so this called procedural Programming 
## Procedural programming is one of the earliest paradigms of Programming.In fact, back in the days when we had older languages like Fortran and COBOL.
## How to use OOP

## Write a code for Restuarant Using with OPP 

## Hired three types of staff and manager who would then managed all of these three different types of staff.
## To model a real world object 

## We probably have to model a virtual chef, waiter, cleaner and manager .
## go to work 
## waiter - has : is_holding_plate = True, tables_responsible = [4,5,6] sheets @ attribute is called 
## basically variable this is fancy variable 
##          does : def take_order(order, table):, def take_payment(amount):@method above two most important
# things that make up an object: it attributes and its methods.

#   {is_holding_plate = True
 #   table_responsible = [4,5,6]} - attributes

#{def take_order(table, order) : # takes order to chef
#def take payment(amount): # add money to restaurant} Method 
 
# Constructing Objects 

#car = CarBlueprint()    # It is creating class  frst letter normally capitalized known as Pascal case.
# car is object 

# from another_module import another_variable

# result = another_variable()
# print(result )

#car (speed, fuel) # in this case car.speed  objes.attribute respectively as work
# import turtle
# print(turtle.Turtle)

# from turtle import Turtle,Screen  # here import another function 
# timmy =Turtle()   # class print message 
# print(timmy)      # object at something message 
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.fd(100)
# go for more study about turtle https://docs.python.org/3/library/turtle.html

# my_screen = Screen()   # another function 
# print(my_screen.canvheight)
# my_screen.exitonclick()

# If Pretty table not install in your system first installed as pip install Prettytable 
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"]) # Add column with header 
table. add_column("Type",["Electric","Water","Fire"])
table.align   # Horizontal alignment 
# for above about more knowledge go through this link https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
print(table)

# OPP version through make a coffee machine code 
