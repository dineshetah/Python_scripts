# import turtle as t 
# import random
# tim = t.Turtle()
# num_sides = 5     # mentioned no of sides 
# colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", 
            #  "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
# def draw_shape(num_sides):
#  angle = 360/ num_sides # find the angle corresponding no of sides
#  for _ in range(num_sides): # this for loop range (num of sides )
#    tim.forward(100)
#    tim.right(angle)
# for shape_side_n in range(2, 11):
#   tim.color(random.choice(colours))
#   draw_shape(shape_side_n)
  #print(draw_shape)
  
  ########################################
  #Draw a Random Walk 
  #https://docs.python.org/3/library/turtle.html#turtle.setheading

import turtle as t 
import random
tim = t.Turtle()
t.colormode()        # define color 
def random_color():
    r = random.randint(0, 255)  # this is for random generates numbers
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    colours = (r,g,b)
    return colours
colours = ["yellow", "gold", "orange", "red", "maroon", "violet"]
directions = [0,90,180,270]  #choose direction E W N S wisetim.pensize(15)    # width of direction
tim.speed("fastest")
for _ in range(200):     # range to walk distance
  #tim.color(random_color())
  tim.forward(30)
  tim.setheading(random.choice(directions))





# Make a Spirograph 

# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# ########### Challenge 5 - Spirograph ########

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)




