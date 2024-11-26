from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time  

screen = Screen()
screen.setup(width=600, height=600)  
screen.bgcolor("black")  
screen.title("Snake Game")  
screen.tracer(0) 
snake = Snake()

food = Food()
scoreboard = Score()

screen.listen()  
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()  
    time.sleep(0.1)  

    snake.move()

    head = snake.all_segments[0]
    if head.distance(food) < 15:  
        food.refresh()  
        snake.extend()
        scoreboard.update_score()

    if head.xcor() > 280 or head.xcor() < -290 or head.ycor() > 280 or head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.all_segments[1:]:  
        if head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()  


0



from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        self.all_segments.append(new_segment)

    def reset(self):
        for segment in self.all_segments:
            segment.goto(1000, 1000)  
        self.all_segments.clear()  
        self.create_snake()

    def extend(self):
        self.add_segment(self.all_segments[-1].position())  

    def move(self):
        for segment_number in range(len(self.all_segments) - 1, 0, -1):  
            new_x = self.all_segments[segment_number - 1].xcor()
            new_y = self.all_segments[segment_number - 1].ycor()
            self.all_segments[segment_number].goto(new_x, new_y)
        self.all_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """turns the first segment facing upwards"""
        if self.all_segments[0].heading() != DOWN:
            self.all_segments[0].setheading(UP)

    def down(self):
        """turns the first segment facing downwards"""
        if self.all_segments[0].heading() != UP:  
            self.all_segments[0].setheading(DOWN)

    def left(self):
        """turns the first segment facing left"""
        if self.all_segments[0].heading() != RIGHT: 
            self.all_segments[0].setheading(LEFT)

    def right(self):
        """turns the first segment facing right"""
        if self.all_segments[0].heading() != LEFT:  
            self.all_segments[0].setheading(RIGHT)



from turtle import Turtle
import random


class Food(Turtle):  

    
    def __init__(self):
        """Initializes a new food object"""
        super().__init__()  
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  
        self.color("blue")
        self.speed("fastest")
        self.refresh()  


    def refresh(self):
        """locates food at a new random location in the screen"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  



from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")  

class Score(Turtle):  
    """a turtle that keeps track of the score and displays the score in the program"""

    def __init__(self):
        """initializes a new scoreboard object"""
        super().__init__() 
        self.score = 0
        self.display_score()

    def display_score(self):
        """displaying sum of points at the top of the screen"""
        self.clear()
        self.goto(0, 280)  
        self.hideturtle()  
        self.color("white")
        with open("data.txt", mode="r") as data:
            high_score = int(data.read())
        self.write(f"SCORE = {self.score} High Score: {high_score} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        with open("data.txt", mode="r") as data:
            high_score = int(data.read())
            if self.score >= high_score:
                with open("data.txt", mode="w") as data:
                    self.score = str(self.score)
                    data.write(self.score)
        self.score = 0
        self.display_score()

    def update_score(self):
        """adds a point to the score and display new score"""
        self.score += 1
        self.clear()
        self.display_score()