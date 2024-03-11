"""Winning card game v1"""

# Imports Easygui and random module
import easygui
import random

game_played = False

while True:
    intro = easygui.buttonbox("Would you like to play?", "Intro "
                              "Screen", ["Yes", "No"])
    if intro == "Yes":
        computer = []
        player = []
        number = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                  "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

        # Generate random combination for computer
        computer_number = random.choice(number)
        computer_suit = random.choice(suits)
        computer_value = number.index(computer_number)

        # While loop to check computer and player don't have same card and fix
        while True:
            # Generate random combination for player
            player_number = random.choice(number)
            player_suit = random.choice(suits)
            player_value = number.index(player_number)
            if computer_value != player_value or computer_suit != player_suit:
                break
            else:
                continue

        # Adds computer and player card to a list
        computer.append(computer_number)
        computer.append(computer_suit)
        player.append(player_number)
        player.append(player_suit)

        # Assigns player number an index
        player_result = number.index(player_number)

        easygui.msgbox(f"The Computer had the {computer[0]} of {computer[1]} "
                       f"and you had the {player[0]} of {player[1]}")

        if computer_value == player_result:
            easygui.msgbox("It was a draw")
        elif computer_value > player_result:
            easygui.msgbox("The computer won")
        else:
            easygui.msgbox("You won")

        game_played = True

    else:
        break

if game_played:
    easygui.msgbox("Thanks for playing\n\n         Goodbye", "Goodbye")
else:
    easygui.msgbox("Goodbye", "Goodbye")
