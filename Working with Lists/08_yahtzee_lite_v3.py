"""Yahtzee Lite v2
Added 2 player system and now counts score
"""

import easygui
import random

dice = ["1", "2", "3", "4", "5", "6"]

player1 = easygui.enterbox("Please enter name of player 1:",
                           "Player 1")
player2 = easygui.enterbox("Please enter name of player 2:",
                           "Player 2")
player1_roll = []
player2_roll = []
player1_score = 0
player2_score = 0

while True:
    number_1 = 0
    number_2 = 0
    while True:
        results = []
        for i in range(5):
            rolled = random.choice(dice)
            results.append(rolled)
        results.sort()
        player1_roll = ", ".join(results)
        if number_1 == 2:
            sequence1 = easygui.buttonbox(f"{player1}: Dice roll "
                                          f"{number_1+1}\nCurrent score "
                                          f"{player1_score}\n\nYou rolled: "
                                          f"{player1_roll}\n\nChoose:",
                                          "Result", ["Stick"])
        else:
            sequence1 = easygui.buttonbox(f"{player1}: Dice roll "
                                          f"{number_1+1}\nCurrent score "
                                          f"{player1_score}\n\nYou rolled: "
                                          f"{player1_roll}\n\nChoose:",
                                          "Result", ["Roll again",
                                                     "Stick"])

        if sequence1 == "Stick":
            three_kind = any(results.count(result) >= 3 for result in results)
            four_kind = any(results.count(result) >= 4 for result in results)
            yahtzee = any(results.count(result) == 5 for result in results)

            if yahtzee:
                easygui.msgbox(f"You rolled: {player1_roll}\n\nYahtzee!",
                               "Winner")
                player1_score += 50
            elif four_kind:
                easygui.msgbox(f"You rolled: {player1_roll}\n\nFour of a "
                               f"kind!", "Winner")
                player1_score += 30
            elif three_kind:
                easygui.msgbox(
                    f"You rolled: {player1_roll}\n\nThree of a kind!",
                    "Winner")
                player1_score += 10
            else:
                easygui.msgbox(f"You rolled: {player1_roll}\n\nBetter"
                               f" luck next time", "Loser")

            break
        else:
            number_1 += 1
            continue

    while True:
        results = []
        for i in range(5):
            rolled = random.choice(dice)
            results.append(rolled)
        results.sort()
        player2_roll = ", ".join(results)
        if number_2 == 2:
            sequence2 = easygui.buttonbox(f"{player2}: Dice roll "
                                          f"{number_2+1}\nCurrent score "
                                          f"{player2_score}\n\n"
                                          f"You rolled: {player2_roll}\n\n"
                                          f"Choose:", "Result",
                                          ["Stick"])
        else:
            sequence2 = easygui.buttonbox(f"{player2}: Dice roll "
                                          f"{number_2+1}\nCurrent score "
                                          f"{player2_score}\n\nYou rolled: "
                                          f"{player2_roll}\n\n"f"Choose:",
                                          "Result", ["Roll again",
                                                     "Stick"])

        if sequence2 == "Stick":
            three_kind = any(results.count(result) >= 3 for result in results)
            four_kind = any(results.count(result) >= 4 for result in results)
            yahtzee = any(results.count(result) == 5 for result in results)

            if yahtzee:
                easygui.msgbox(f"You rolled: {player2_roll}\n\nYahtzee!",
                               "Winner")
                player2_score += 50
            elif four_kind:
                easygui.msgbox(f"You rolled: {player2_roll}\n\nFour of a "
                               f"kind!", "Winner")
                player2_score += 30
            elif three_kind:
                easygui.msgbox(
                    f"You rolled: {player2_roll}\n\nThree of a kind!",
                    "Winner")
                player2_score += 10
            else:
                easygui.msgbox(f"You rolled: {player2_roll}\n\nBetter"
                               f" luck next time", "Loser")

            break
        else:
            number_2 += 1
            continue

    if player2_score > player1_score:
        winner = easygui.buttonbox(f"The winner is {player2}! with a "
                                   f"score of {player2_score}\n\n{player1} "
                                   f"scored {player1_score}\n\nWould you "
                                   f"like to play another round?",
                                   "Result", ["Yes", "No"])
        if winner == "Yes":
            continue
        else:
            break
    elif player1_score > player2_score:
        winner = easygui.buttonbox(f"The winner is {player1}! with a "
                                   f"score of {player1_score}\n\n{player2} "
                                   f"scored {player2_score}\n\nWould you "
                                   f"like to play another round?",
                                   "Result", ["Yes", "No"])
        if winner == "Yes":
            continue
        else:
            break
    else:
        winner = easygui.buttonbox(f"This is a draw!\n\n{player1} scored "
                                   f"{player1_score} and {player2} scored "
                                   f"{player2_score}\n\nWould you like to "
                                   f"play another round?", "Result",
                                   ["Yes", "No"])
        if winner == "Yes":
            continue
        else:
            break

easygui.msgbox("Thanks for playing", "Thanks")
