print("Welcome to the treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input("You have come to an lake. There is an Island in the middle of the lake. type 'wait' to wait for the boat or type 'swim' to swim across.").lower()
    if choice2 == "wait":
        choice3 = input("You have arrived at the island unharmed by the boat. There is a house with the three doors. One red, one blue and one yellow. Which color do you choose?").lower()
        if choice3 == "red":
            print("It's a room full of fire. You are burned to death. Game Over!!!")
        elif choice3 == "blue":
            print("You have enterd a room full of poison. You died by posion. Game Over!!!")
        elif choice3 == "yellow":
            print("Congrulation... You have found the treasure full of gold and dimonds...")
        else :
            print("You choose the door that doesnt exist. Now you are lost in another dimension. Game Over!!!")
    else:
        print("You got attacked by the  monster!. Game Over!!! ")
else: 
    print("You fell into a trap!. Game Over!!!")