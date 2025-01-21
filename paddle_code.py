from turtle import Turtle
#from paddle_code import Paddle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        
        paddle = Turtle()
        paddle.shape("square")    # use for shape any type mention
        paddle.color("white")     # use for color any type mention 
        paddle.shapesize(stretch_wid=5, stretch_len=1)  # shapesize function
        paddle.penup()        # use move to turtle any where
        paddle.goto(position)    # goto with x, y coordinate 

    def go_up(self):      # this self attribute for Paddle class use self instead of paddle place 
        new_y = self.ycor() + 20 
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20 
        self.goto(self.xcor(),new_y)