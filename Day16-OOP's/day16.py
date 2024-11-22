# # Su Feb 27, 2022 and Mo Feb 28, 2022
# # Day 16. Learning about Object Oriented Programming (OOP)
#
# import another_module
#
# print(another_module.another_variable)
#
# # Import module named 'turtle'
# # import turtle
# # Call class inside the turtle and put it in an object names 'timmy'
# # A class always starts with capitals and does not use underscores:
# # timmy = turtle.Turtle()
#
# # or shorter:
# from turtle import Turtle, Screen
# timmy = Turtle() # create a new object 'timmy' from blueprint Turtle()
# print(timmy)
#
# # Call methods associated with the object:
# timmy.shape("turtle") # change shape of timmy to a turtle
# timmy.color("chartreuse2") # change color of timmy
# timmy.forward(100) # move timmy forward with 100 steps
# # Screen is a class that represents the window in which the turtle is going to show up
# # Create object 'my_screen'
# my_screen = Screen()  # create from blueprint Screen()
# # showing: '300' wich is the height of the canvas of the screen created:
#
# # Tab in attributes associated with the object:
# print(my_screen.canvheight)  # object.attribute
#
# # Object methods:
# my_screen.exitonclick()
# """Instead of screen just showing up for a second
# will allow our program to continue running, until we click on the screen"""
# # Turtle in the form of a arrow in the middle. This is timmy
# # Changed timmy into a tuurtle by 'timmy.shape("turtle')

# D16. 148
# Installed PrettyTable manually via Preferences - Project: day-16-1start

# From the prettytable package, import class PrettyTable:
from prettytable import prettytable

# Create object 'table' from class PrettyTable:
table = prettytable.PrettyTable()
print(table)

# Add two columns "Pokemon Name" and "Type" to the table:
# This is tapping in the methods of the object "table"
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'], align = "l")
table.add_column('Type', ['Electric', 'Water', 'Fire'], align)
print(table)

# Text is center aligned -> Align the text to the columns to the left:
# Tap into the attributes of the object "table"
print(table.align)