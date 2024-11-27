
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time  

screen = Screen()
screen.setup(width=800, height=600)  
screen.bgcolor("black")  
screen.title("Pong Game") 
screen.tracer(0)  

l_paddle = Paddle(start_x=-350, start_y=30)

r_paddle = Paddle(start_x=350, start_y=30)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()  
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()  
    time.sleep(0.1)  
    r_paddle = r_paddle

    ball.move()  

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_wall()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -335 or ball.distance(r_paddle) < 50 and ball.xcor() > 335:
        ball.bounce_paddle()

    if ball.xcor() < -430:
        scoreboard.update_score_left()
        ball.clear()
        ball = Ball()

    if ball.xcor() > 430:
        scoreboard.update_score_right()
        ball.clear()
        ball = Ball()

screen.exitonclick()  



from turtle import Turtle

UP = 90  
DOWN = 270 
MOVE_DISTANCE = 20 


class Paddle(Turtle): 
    
    def __init__(self, start_x, start_y):
        super().__init__() 
        self.shape("square") 
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setposition(start_x, start_y)
        self.color("white")
        self.setheading(UP)  

    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        self.setheading(UP)
        self.move()

    def down(self):
        self.setheading(DOWN)
        self.move()


from turtle import Turtle
import random


UP = 90  
LEFT = 180 
DOWN = 270  
MOVE_DISTANCE = 10 
START_X = 0
START_Y = 0


class Ball(Turtle): 

    def __init__(self):
        super().__init__()  
        self.shape("circle")
        self.penup()  
        self.goto(START_X, START_Y) 
        self.shapesize(stretch_len=1, stretch_wid=1) 
        self.color("white")
        self.moving_speed = MOVE_DISTANCE  
        self.speed("normal")  
        random_direction = random.randint(0, 360)
        self.setheading(random_direction)

    def move(self):
        self.forward(self.moving_speed)

    def bounce_wall(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)
        self.move()

    def bounce_paddle(self):
        ball_heading = self.heading() + 180
        self.setheading(ball_heading)
        self.move()
        self.increase_ball_speed()

    def increase_ball_speed(self):
        self.moving_speed += 5


from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")  
LOCATION = (0, 280)
MAXIMUM_POINTS = 10


class Scoreboard(Turtle):  
    
    def __init__(self):
        super().__init__()  
        self.score_left = 0
        self.score_right = 0
        self.display_score()

    def display_score(self):
        self.goto(LOCATION)
        self.hideturtle()  
        self.color("white")
        self.write(f"SCORE = {self.score_left} | {self.score_right}", align=ALIGNMENT, font=FONT)

    def update_score_left(self):
        self.score_left += 1
        self.clear()
        self.display_score()

    def update_score_right(self):
        self.score_right += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)  
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)