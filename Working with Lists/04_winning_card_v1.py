"""Winning card game v1"""

import easygui
import random

computer = []
player = []
number = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
          "Ten", "Jack", "Queen", "King", "Ace"]
suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

# Generate random combination for computer
computer_number = random.choice(number)
computer_suit = random.choice(suits)
computer_value = number.index(computer_number)

# Removes computer number from list
number.pop(computer_value)

# Generate random combination for player
player_number = random.choice(number)
player_suit = random.choice(suits)

# Adds computer and player card to a list
computer.append(computer_number)
computer.append(computer_suit)
player.append(player_number)
player.append(player_suit)

player_result = number.index(player_number)

easygui.msgbox(f"The Computer had the {computer[0]} of {computer[1]} and "
               f"you had the {player[0]} of {player[1]}")
if computer_value > player_result:
    easygui.msgbox("The computer won")
else:
    easygui.msgbox("You won")
