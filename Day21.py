# CLASS INHERITANCE 

class Fish:          # this in initializer class
    def __init__(self):
        pass

class Fish(Animal):          # this in initializer inside the parenthesis another class 
    def __init__(self):
        super().__init__()    # have to do is inside the init, add this super().__init__()
        pass

# Write a code using class and with define function 
    
class Animal:   # this is first class created 
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale","Exhale")

#class Fish:    # Another second class created
class Fish(Animal):
    def __init__(self):
        super().__init__()    # this initiallized allowed to anythings 
        super().breathe()   # this for under work breathe function using super class or method 
        print("Doing this underwater")
        
    def swim(self):
        print("moving in water")
demo = Fish()  # assigned new variable as equal class name 
demo.swim()  # attribute and method with Class  from the superclass inherited from the animal class 
demo.breathe()
print(demo.num_eyes)



#Question 3: Given this code:

class Dog:
    def __init__(self):
        self.temperament = "loyal"
 
    def bark(self):
        print("Woof, woof!")
 
class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True
 
    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")


#What will this print?

sparky = Labrador()
sparky.bark()


## Question 1:Given the following:

class Dog:
    def __init__(self):
        self.temperament = "loyal"
 
    def bark(self):
        print("Woof, woof!")
#How do you create a class called Labrador (the subclass) that inherits from the Dog class (the superclass)?
class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "friendly"

# ## Question 2:Given this:

class Dog:
    def __init__(self):
        self.temperament = "loyal"
 
class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"

# ## What will this code print?
doggo = Dog()
print(f"A dog is {doggo.temperament}")
 
sparky = Labrador()
print(f"Sparky is {sparky.temperament}")

from turtle import  Turtle, Screen
from main_snake import Snake 
from food_source import Food
from scoreboard import Scoreboard
import time
turtle = Turtle()
screen = Screen()
screen.setup(width = 600, height =600)  # set dimenstion of displace 
screen.bgcolor("black")  # assigned backgroud color 
screen.title("My Snake Game")  # assigned the title name 
screen.tracer(0)

main_snake = Snake()
food_source = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(main_snake.up, "Up")
screen.onkey(main_snake.down, "Down")
screen.onkey(main_snake.left, "Left")
screen.onkey(main_snake.right, "Right")

game_is_on = True

while game_is_on:
    #turtle.heading()
    screen.update()
    time.sleep(0.1)
    main_snake.move()
    

    #Detect collision with food.
    if main_snake.head.distance(food_source) < 15:
        food_source.refresh()
        main_snake.extend()
        scoreboard.increase_score()


    # # Detect collision with food.
    if main_snake.segments[0].distance(food_source) < 15:
        food_source.refresh()
        main_snake.extend()
        scoreboard.increase_score()
    
     #Detect collision with wall.
    #if main_snake.head.corr() > 280 or main_snake.head.xcor() < -280 or main_snake.head.ycor() > 280 or main_snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    #Detect collision with tail.
    for segment in main_snake.segments:
        if segment == main_snake.head:
            pass
        elif main_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
    screen.exitonclick()