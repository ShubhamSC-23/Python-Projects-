# We Feb 16, 2022
# Day 11 - BlackJack 

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # The items in the list are integers 
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Only use Hint 1 for expert level: 

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

# My code:
import random 
from replit import clear
play = True 

def bj_winner(player, computer): 
    """Function that calculates the full score of player and computer, and
    determines the winner"""
    print(f"\nYour cards: {player_list}, final score {sum_player}\nComputer\'s final hand: {computer_list}, final score {sum_computer}")
    winner(player = sum_player, computer = sum_computer)

def winner(player, computer):
    """Defines who is the winner of the game"""
    if player == 21 and computer != 21:
        print("You win!")
    elif player <= 21 and computer == player:
        print("It's a draw!")
    elif player > 21:
        print("You went over. You lose!")
    elif player != 21 and computer == 21:
        print("Computer wins!")
    elif player > computer:
        print("You win!")
    elif computer > player:
        print("Computer wins!")

while play: 
    start = input("Do you want to play a game of Black Jack? Type \'y\' or \'n\': ")
    if start == "y":
        blackjack = True
        clear() 
        print(logo)
    elif start == "n":
        blackjack = False 
        play = False 
    # A while loop to continue blackjack while it is True 
    player_list = [] # Create emply list for player
    player_list.append(random.choice(cards))
    computer_list = [] # Create empty list for computer
    computer_list.append(random.choice(cards))
    
    while blackjack:
        player_list.append(random.choice(cards))
        computer_list.append(random.choice(cards))

        # Make if loop for if last card is 11 for player:
        len_player = int(len(player_list))
        if player_list[len_player - 1] == 11:
            if sum_player + 11 > 21:
                player_list[len_player - 1] = 1
            else:
                player_list[len_player - 1] = 11
        # Make an if statement for if last card is 11 for computer:
        len_computer = int(len(computer_list))
        if computer_list[len_computer - 1] == 11:
            if sum_computer + 11 > 21:
                computer_list[len_computer - 1] = 1
            else:
                computer_list[len_computer - 1] = 11
            
        sum_player = 0
        sum_computer = 0 
        for card in player_list:
            sum_player += card # Add value of each new card to total sum 
        for card in computer_list:
            sum_computer += card
        print(f"\nYour cards: {player_list}, current score {sum_player}\nComputer\'s first card: {computer_list[0]}")
    
        if sum_player >= 21:
            blackjack = False 
            bj_winner(player = sum_player, computer = sum_computer) 
    
        else: 
            bj_continue = input("Type \'y\' to get another card, type \'n\' to pass: ")
            if bj_continue == "y":
                blackjack = True
            elif bj_continue == "n":
                blackjack = False 
                bj_winner(player = sum_player, computer = sum_computer) 