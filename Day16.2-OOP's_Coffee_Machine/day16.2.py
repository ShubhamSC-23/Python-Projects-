# Mo Feb 28, 2022 and Tu March 1, 2022
# Day 16. OOP Coffee Machine

# Goal. You do not touch any of the other files besides main.py
# So don't touch money_machine.py, menu.py or coffee_maker.py
# Treat them as an external library


# # Import Classes from packages/modules:
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# # Create objects from the blueprints of the Classes
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_is_on = True

while machine_is_on:
     choice = input(f"What would you like? {menu.get_items()}?: ").lower()
     if choice == "off":
         machine_is_on = False

     elif choice == "report":
         coffee_maker.report()
         money_machine.report()

     elif choice == "espresso" or "latte" or "cappuccino":
         drink = menu.find_drink(choice)
         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                 coffee_maker.make_coffee(drink)