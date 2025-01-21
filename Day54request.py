# import requests
# requests.get("https:/www.google.com")

# from flask import Flask
# import random
# app = Flask(__name__)
# print(random.__name__)
# print(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello, World!"
# if __name__=="__main__":
#     app.run()


## Python Decorators ##
# Q. what exactly is a Decorators
# A. lets imagine that you have a bunch of functions in your class or in your class or module 
# and you want to add some functionality to each of these functions

# Functions can have inputs/functionality/output

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#functions are First-class objects, can be passed around as arguments e.g. int/string/float etc.

# def calculate(calc_function,n1,n2):
#     return calc_function(n1,n2)
# result = calculate(add, 2, 3)
# print(result)

#Nested Functions 

# def outer_function():
#     print("I'm outer")

#     def Nested_function():
#         print("I'm inner")
# #Nested_function() # here we will get error 
#         Nested_function() # here will not be get error 
#     return Nested_function

# inner_function = outer_function()
# inner_function()

## Python Decorator function 

import time 
def delay_decorat(function):
    def wrapper_function():
        time.sleep(2)
        function
    return wrapper_function

def say_hellow():
    print("Hello")

def say_bye():
    print("Bye")

def say_greeting():
    print("How are you ?")


## Variable Rules:
# You can add variable section to a URL by marking sections with <variable_name>
# Your function recieves the <variable_name> as a keyword argument.
# Optionally, you can use a converter to specify the type of the argument like
# <convert:variable_name
    
from markupsafe import escape
@app.route('/user/<username>')

def show_user_profile(username):
    #show the user profile for that user
    return 'User %s'% escape(username)


