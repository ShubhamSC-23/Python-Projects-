import random
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [Rock,Paper,Scissors]

user_choice = int(input("Enter your choice: (for rock put 0, for paper put 1 and for scissors put 2)"))
if  user_choice > 2 or  user_choice < 0 :
    print("Invalid choice .. You lose..!")
else:
    print("You chose :", game[user_choice])

    comp_choice = random.randint(0,2)
    print("Computer chose:", game[comp_choice])

    if user_choice == 0 and comp_choice == 2:
        print("You win !!")
    elif user_choice == 2 and comp_choice == 0:
        print("You lose ...")
    elif user_choice == 1 and comp_choice == 0:
        print("You win!!")
    elif user_choice == 0 and comp_choice == 1:
        print("You lose...")
    elif user_choice == 2 and  comp_choice == 1:
        print("You lose ...")
    elif user_choice == 1 and  comp_choice == 2:
        print("You win ...")
    else:
        print("It is a draw ....")