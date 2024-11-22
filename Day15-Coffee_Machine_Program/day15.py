# We Feb 23, 2022 and Fr Feb 25, 2022
# Day 15. The Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": [0, ]
}

profit = [0]

# coins = {
#     "quarter": 0,
#     "dimes": 0,
#     "nickel": 0,
#     "pennies": 0,
# }

# Functions:

def resources_value():
    """Substracts used resources. Adds profit. Returns the resources report"""
    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    return f"Water: {water_left}\nMilk: {milk_left}\nCoffee: {coffee_left}\nMoney: {sum(profit)}"

def enough_resources_left(drink):
    """Function compares the resources left and the resources needed for the drink.
     If enough resources left it returns a True statement.
     If not enough resources left it returns what is missing"""
    if "milk" in MENU[drink]["ingredients"]:
        if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            return "Sorry, there is not enough milk."
    if resources["water"] < MENU[drink]["ingredients"]["water"] < 0:
        return "Sorry, there is not not enough water."
    if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        return "Sorry, there is not enough coffee"
    else:
        return True  # Makes it a True statement

def enough_money(money, drink):
    """Compares the amount of money added to the money needed.
     If not enough money it returns the refund.
     If enough money, the cost of drink gets added to the machine and a True statement is returned
     If too much money,the cost of the drink is added to the machine, the extra money is returned and a True statement
     is returned"""
    if money < MENU[drink]["cost"]:
        return "Sorry, that is not enough money. Money refunded. "
    elif money == MENU[drink]["cost"]:
        profit.append(MENU[drink]['cost'])  # Add money to the profit
        print(profit)
        return True
    elif money > MENU[drink]["cost"]:
        extra_money = money - MENU[drink]["cost"]
        return f"Here is ${round(extra_money, 2)} in change. "  # Change is rounded to 2 decimals
        profit.append(MENU[drink]['cost'])
        print(profit)
        return True

def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!" )

# Variables:
coffee_machine_on = True

# TODO: 1. Prompt user by asking: "What would you like? (espresso/latte/cappuccino):"
while coffee_machine_on:
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the coffee machine by entering "off" to the prompt
    if answer == "off":
        coffee_machine_on = False

    # TODO: 3. Print report of all coffee machine resources. By entering "report: to the prompt
    elif answer == "report":
        # output = resources_value()
        # print(output)
        print(resources_value())

    # TODO: 4. Check resources sufficient to make drink order
    elif answer == "espresso" or "latte" or "cappuccino":
        # print(enough_resources_left(drink = answer))

    # TODO: 5. Process coins
        if enough_resources_left(drink = answer): # This should be True if there is enough resources
            insert_quarters = float(input("Please insert coins.\nHow many quarters?: "))
            insert_dimes = float(input("How many dimes?: "))
            insert_nickles = float(input("How many nickles?: "))
            insert_pennies = float(input("How many pennies?: "))
            sum_coins = insert_quarters * 0.25 + insert_dimes * 0.10 + insert_nickles * 0.05 + insert_pennies * 0.01

        # TODO: 6: Check transaction successful?
        # TODO: 7: Make coffee
            if sum_coins < MENU[answer]["cost"]:
                print("Sorry, that is not enough money. Money refunded. ")
            elif sum_coins == MENU[answer]["cost"]:
                profit.append(MENU[answer]['cost'])  # Add money to the profit
                drink = MENU[answer]
                make_coffee(drink_name= answer, order_ingredients= drink['ingredients'])
            elif sum_coins > MENU[answer]["cost"]:
                extra_money = sum_coins - MENU[answer]["cost"]
                print(f"Here is ${round(extra_money, 2)} in change. ") # Change is rounded to 2 decimals
                profit.append(MENU[answer]['cost'])
                drink = MENU[answer]
                make_coffee(drink_name= answer, order_ingredients= drink['ingredients'])