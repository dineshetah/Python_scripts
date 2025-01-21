# working with CSV files and Analysing Data with Pandas 
# Go to google side and create weather_data 


# with open("C:\\Users\DC Yadav\\Desktop\\weather_data.csv", "r") as data_file:
#     data =data_file.readline()
# print(data)
 
import csv

# with open("C:\\Users\DC Yadav\\Desktop\\weather_data.csv", "r") as data_file:
#     data =csv.reader(data_file) 
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append((row[1]))
        
#     print(temperature)

# For data anaylisy need to import pandas library 
import pandas as pd # mentioned the pandas library module 
file = "C:\\Users\KIIT\Desktop\\100Days_code_programming\\weather_data.csv"  # mentioned file path 
data = pd.read_csv(file) # using with pandas object  functions and methods 
# print(data.columns)
# print(data["Condition"])
# print(data["temp"])
# go to https://pandas.pydata.org/docs/reference/index.html for more knowledge
## go to Data Frame inside above link 

# data_dict = data.to_dict()
# print(data_dict)   # print out the new data dictionary 

# temp_list = data["Temp"].to_list()   # here data seriers into a python list 
# print(temp_list)  # print out the temperature data in a list format
# print(len(temp_list)) 
# avg_temp =sum(temp_list)/len(temp_list)
# print(avg_temp)

# print(data["Temp"].mean()) # for calculate mean temperature 
# print(data["Temp"].max()) # for calculate 

# Get Data in Columns 
#data[""]  # Here inside Data frame specify the name of the column

#print(data["Day"])
#print(data.Day)       # Both are getting result 

# Get Data in Row 
# print(data[data.Day == "Monday"].index)

# Print unique values in the "Day" column
#print(data["Day"].unique())

# Get entire row(s) based on a condition  boolean mask's index. data.iloc[...]
# monday_data = data.iloc[(data["Day"] == "Monday").index]
# print(monday_data)

# Get entire row by index (e.g., index 0)
# row_data = data.iloc[0]
# print(row_data)

# temp_max = data[data.Temp == data.Temp.max()]  # Here data attribute how to use for entire row data 
# print(temp_max)

monday = data[data.Day == "Monday"]
# print(monday.Temp)

# Here temperature are in Celsius to convert it into Fahrenheit

# monday_temp = monday.Temp[0]
# monday_f = monday_temp* 9/5 + 32
# print(monday_f)

# Create a dataframe from scratch 
data_dict = { 'student':['Army','James', 'Angela'],'scores': [76, 56, 65]
    }
pd.DataFrame(data_dict)     # Here is created data 

data =pd.DataFrame(data_dict)
print(data)  # Here print out the data from dictionary 
data.to_csv("new_data.csv") # Here you can get new_data file in csv format 

# Here you can download data from this link https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

##  US game start 

import turtle
import pandas as pd
screen = turtle.Screen()  # Create the screen with attribute turtle
screen.title("U.S. States Game")  # title of the game here
image = "blank_states_img.gif" # here my image file name mentioned 

screen.addshape(image)  # add screen on image 
turtle.shape(image)
data = pd.read_csv("50_states.csv")
#data["state"] # or you can use 

all_state = data.state.to_list()
# Here the below variable answer_state for popup can user enter the input values 

guessed_states = []  # Here is blank list 
while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len (guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    #print(answer_state)
    if answer_state == "Exit":  # this is for guess exit 
        missing_states = []   # this is assigned for blank list 
        for state in all_state: # for loop for missing states 
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learned.csv")
        print(missing_states)
        break
# Here we check to see if the answer_state is in the all_states 
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()  # use the tutle.Turtle class object  to construct it 
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # state_data variable This is here going to pull out the row where the state is equal to the answer state 
        t.goto (int(state_data.x), int(state_data.y))
        t.write(answer_state)  # Here is mentioned answer_State inside write 
turtle.done()
# def get_mouse_click_coor(x, y): # defined mouse click on function 
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor) # Here the turtle moudule with using mouse cocrdinate function\

# turtle.mainloop()


#screen.exitonclick()

# Here there are  6 step follwoing
# 1. convert the guess to Title case
# 2. Check if the guess is among the 50 states 
# 3. Write correct guesses onto the map 
# 4. Use a loop to allow the user to keep guessing 
# 5. Record the correct guesses in a list 
# 6. Keep track of the score 
