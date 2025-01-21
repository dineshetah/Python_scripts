from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake: 
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        #self.heading()
    
    def create_snake(self):
        for position in STARTING_POSITIONS: # this for loop creates Snake 
            #segment_1 = Turtle("square")
            new_Segment =Turtle("square")
            new_Segment.color("white")
            new_Segment.penup()
            new_Segment.goto(position)
            self.segments.append(new_Segment)
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1) :# actually to go from 2,1,0 instead of 3,2,1
            new_x = self.segments[seg_num-1].xcor()  # this for first segments with new variable get hold it xcor
            new_y = self.segments[seg_num-1].ycor() # this for second last segments with new variable get hold it xcor
            self.segments[seg_num].goto(new_x,new_y)

        self.segments[0].forward(MOVE_DISTANCE)  # 20 paces move forward 
            #self.segments[0].left(90) # left turn with 90 degree
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)