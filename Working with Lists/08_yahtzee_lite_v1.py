"""Yahtzee Lite v1"""

import easygui
import random

number = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
          "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
round_1 = 0

while True:
    deck = []
    for suit in suits:
        for card in number:
            deck.append([card, suit])
    random.shuffle(deck)
    draw = []
    for card in deck[0:7]:
        draw.append(f"Card {deck.index(card)+1}: {card[0]} of {card[1]}")

    show_cards = ""
    for item in draw:
        show_cards = f"\n-    ".join(draw)
    round_1 += 1
    play_again = easygui.buttonbox(f"Round {round_1}:\nYou have drawn:\n\n"
                                   f"-    {show_cards}\n\nWould you like to "
                                   f"play again?", "Result",
                                   ["Yes", "No"])
    if play_again == "Yes":
        continue
    else:
        break
easygui.msgbox("Thank you for using this program", "Goodbye")
