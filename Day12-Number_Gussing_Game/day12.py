# Fr Feb 18, 2022
# Day 12 (D12.120) - The number guessing game

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Import modules: 
import random
from replit import clear

# Create starting logo: 
# From http://patorjk.com/software/taag/#p=display&h=1&f=Slant%20Relief&t=Guess%20The%20Number 
logo = """

                                                                )                                      
 (                                   *   )      )            ( /(                      )               
 )\ )       (      (               ` )  /(   ( /(     (      )\())    (       )     ( /(     (    (    
(()/(      ))\    ))\   (    (      ( )(_))  )\())   ))\    ((_)\    ))\     (      )\())   ))\   )(   
 /(_))_   /((_)  /((_)  )\   )\    (_(_())  ((_)\   /((_)    _((_)  /((_)    )\  ' ((_)\   /((_) (()\  
(_)) __| (_))(  (_))   ((_) ((_)   |_   _|  | |(_) (_))     | \| | (_))(   _((_))  | |(_) (_))    ((_) 
  | (_ | | || | / -_)  (_-< (_-<     | |    | ' \  / -_)    | .` | | || | | '  \() | '_ \ / -_)  | '_| 
   \___|  \_,_| \___|  /__/ /__/     |_|    |_||_| \___|    |_|\_|  \_,_| |_|_|_|  |_.__/ \___|  |_|   
                                                                                                       
                                                                        
"""

# Starting up: 
clear() 
print(logo)
print("Welcome to the Number Guessing Game!")
print("I\'m thinking of a number between 1 and 100.")
RANDOM_NUMBER = random.randint(1, 100) # Create a global random integer between 1 and 100, including 1 and 100 

# Defining the level: 
level = input("Choose a difficulty. Type \'easy\' or \'hard\': ")
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
print(f"You have {attempts} attempts remaining to guess the number")

# Make a global list for the number of attempts/guesses:
guesses = []
stop = []

# Guessing a number: 
def make_a_guess(): 
    """Function to guess a number to compare with RANDOM_NUMBER. 
    At the same time it adds a number to the global list guesses"""
    guess = int(input("Make a guess: "))
    guesses.append(1) # Add attempts to the global list guesses 
    return guess

# Function to compare guess with the RANDOM_NUMBER: 
def compare_numbers():
    """Function that compares the guessed number with the RANDOM_NUMBER.
    Output will tell if the guessed number is higher or lower compared to 
    the RANDOM_NUMBER"""
    if global_number < RANDOM_NUMBER:
        print("\nToo low.\nGuess again. ")
        print(f"You have {attempts - sum(guesses)} attempts remaining to guess the number. ")
    elif global_number > RANDOM_NUMBER:
        print("\nToo high.\nGuess again. ")
        print(f"You have {attempts - sum(guesses)} attempts remaining to guess the number. ")
    elif global_number == RANDOM_NUMBER:
        print(f"\nCorrect.\nYou got it! The answer was {RANDOM_NUMBER}.")
        stop.append(1)
    
# A while loop that keeps going until out of attempts:
while sum(guesses) != attempts and sum(stop) != 1: 
    global_number = make_a_guess()
    compare_numbers()

if sum(guesses) == attempts:
    print("\nYou\'ve run out of guesses, you lose. ")