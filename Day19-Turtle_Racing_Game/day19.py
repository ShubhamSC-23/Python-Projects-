from turtle import Turtle, Screen, _Screen
import random

is_race_on = False
screen = Screen()  
screen.setup(width=500, height=400)  
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x = -225
y = 150
for index in range(0, 6):  
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.color(colors[index])
    all_turtles.append(new_turtle)  
    y -= 50

if user_bet:  
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False  
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You\'ve won! The {winning_color} turtle is the winner! ")
            elif winning_color != user_bet:
                print(f"You lose. The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)  
        turtle.forward(random_distance)   

screen.exitonclick()  