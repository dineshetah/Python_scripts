piano_keys = ["a","b","c","d","e","f","g"]    # this is keys values 
piano_tuples = ("do","re","mi","fa","so","la","ti") # this is tuples 
print(piano_keys[2:5:2])

print(piano_tuples[2:5:2])

## How to create pong game 

# Create the screen 
# Create and move a paddle 
# Create anothe paddle 
# Create the ball and make it move 
# Detect collision with wall and bounce 
# Detect collision with paddle 
# Detect when paddle misses 
# Keep score 

# Create the screen
from turtle import Turtle, Screen
from paddle_code import Paddle
from Ball_code import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=680)
screen.title("Pong")
screen.tracer(0)
# Create and move a paddle 

paddle = Turtle()
# paddle.shape("square")    # use for shape any type mention
# paddle.color("white")     # use for color any type mention 

# paddle.shapesize(stretch_wid=5, stretch_len=1)  # shapesize function
# paddle.penup()        # use move to turtle any where
# paddle.goto(350,0)    # goto with x, y coordinate 



# def go_up(self):      # this self attribute for Paddle class use self instead of paddle place 
#     new_y = self.ycor() + 20 
#     self.goto(self.xcor(),new_y)

# def go_down(self):
#     new_y = self.ycor() - 20 
#     self.goto(self.xcor(),new_y)

## Create another paddle 
r_paddle = paddle((350, 0))   # x, y coordinate assgined with paddle inside 
l_paddle = paddle((-350, 0))  # x, y coordinate assgined with paddle inside 
Ball_code = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    Ball_code.move()



screen.exitonclick()