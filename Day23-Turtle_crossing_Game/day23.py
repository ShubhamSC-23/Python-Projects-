
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()  
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)  

player = Player()
car = CarManager()
car.randomly_create_cars()
score = Scoreboard()

screen.listen()  
screen.onkey(key="Up", fun=player.move)

game_is_on = True
number_while_loops = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.move()
    if number_while_loops % 6 == 0:
        car.randomly_create_cars()

    if player.ycor() > 280:
        player.turtle_crossed()
        score.update_level()
        car.increase_speed_cars()

    for x in car.cars:
        if player.distance(x) < 20:
            game_is_on = False
            score.game_over()

    number_while_loops += 1

screen.exitonclick()


import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
START_X = 300 
LEFT = 180  


class CarManager(Turtle):  

    def __init__(self):
        super().__init__() 
        self.hideturtle()  
        self.cars = []
        self.moving_distance = STARTING_MOVE_DISTANCE
        self.increment_speed = MOVE_INCREMENT

    def create_cars(self):
        car = Turtle(shape="square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)  
        car.penup()  
        car.setheading(LEFT)  
        start_y = random.randint(-250, 250)  
        car.goto(START_X, start_y)
        return self.cars.append(car)

    def randomly_create_cars(self):
        random_create_car = [True, False]  
        do_create_car = random.choice(random_create_car)
        if do_create_car:
            return self.create_cars()  

    def move(self):
        for car_number in range(len(self.cars)-1):
            self.cars[car_number].forward(self.moving_distance)

    def increase_speed_cars(self):
        self.moving_distance += self.increment_speed



from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90  


class Player(Turtle):  

    def __init__(self):
        super().__init__() 
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.color("green")
        self.penup()  
        self.goto(STARTING_POSITION)
        self.setheading(UP)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def turtle_crossed(self):
        self.clear()
        self.create_turtle()


from turtle import Turtle


FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
SCOREBOARD_LOCATION = (-280, 260)  


class Scoreboard(Turtle):  

    def __init__(self):
        super().__init__()  
        self.penup()
        self.level = 1
        self.display_level()

    def display_level(self):
        self.goto(SCOREBOARD_LOCATION)
        self.hideturtle()  
        self.color("black")
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        self.goto(-50, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)