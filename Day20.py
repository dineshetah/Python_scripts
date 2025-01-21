from turtle import  Turtle, Screen
from main_snake import Snake 
import time
screen = Screen()
screen.setup(width = 600, height =600)  # set dimenstion of displace 
screen.bgcolor("black")  # assigned backgroud color 
screen.title("My Snake Game")  # assigned the title name 
screen.tracer(0)

snake = Snake()
# Here to tackle the first of our seven steps"
# starting_positions = [(0, 0), (-20, 0),(-40, 0)] # set variable for starting_positions for different location 
# segments = []
# for position in starting_positions: # this for loop creates Snake 
#     segment_1 = Turtle("square")
#     new_Segment =Turtle("square")
#     new_Segment.color("white")
#     new_Segment.penup()
#     new_Segment.goto(position)
#     segments.append(new_Segment)

    ## Create the snake body
    # segment_1 = Turtle("square")
    # segment_1.color("white")  #white square at the center, which is at position (0,0)
    # ## move the snake 

    # segment_2 = Turtle("square")
    # segment_2.color("white")
    # segment_2.goto(-20,0)    # go to x=-20, y= 0 coordinate

    # segment_3 = Turtle("square")
    # segment_3.color("white")
    # segment_2.goto(-40,0)       # go to x=-40, y= 0 coordinate

game_is_on = True               # this from to end scenarios move Snake 
#my_time = 5
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

#  for seg in segments:
#      seg.forward(20)
#      #screen.update()
#  segments[0].left(90)
 #for seg_num in range(start = 2 , stop= 0, step =-1) :# actually to go from 2,1,0 instead of 3,2,1
#  for seg_num in range(len(segments)-1,0,-1) :# actually to go from 2,1,0 instead of 3,2,1
#      new_x = segments[seg_num-1].xcor()  # this for first segments with new variable get hold it xcor
#      new_y = segments[seg_num-1].ycor() # this for second last segments with new variable get hold it xcor
#      segments[seg_num].goto(new_x,new_y)

#      segments[0].forward(20)  # 20 paces move forward 
#      segments[0].left(90) # left turn with 90 degree


## create snake food
##Detect collision with foood 
## create  a scoreboard 
## Detect collision 
## Detect collision with wall 
## Detect collision with tail

