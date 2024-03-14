"""Yahtzee Lite v1"""

import easygui
import random

dice = ["1", "2", "3", "4", "5", "6"]
number = 0

while True:
    results = []
    for i in range(5):
        rolled = random.choice(dice)
        results.append(rolled)
    results.sort()
    final_result = ", ".join(results)
    sequence = easygui.buttonbox(f"You have rolled: {final_result}\n\n"
                                 f"Choose:", "Result",
                                 ["Roll again", "Stick"])
    if sequence == "Stick" or number == 2:
        three_kind = any(results.count(result) >= 3 for result in results)
        four_kind = any(results.count(result) >= 4 for result in results)
        yahtzee = any(results.count(result) == 5 for result in results)

        if yahtzee:
            easygui.msgbox(f"You rolled: {final_result}\n\nYahtzee!",
                           "Winner")
        elif four_kind:
            easygui.msgbox(f"You rolled: {final_result}\n\nFour of a "
                           f"kind!", "Winner")
        elif three_kind:
            easygui.msgbox(f"You rolled: {final_result}\n\nThree of a kind!",
                           "Winner")
        else:
            easygui.msgbox(f"You rolled: {final_result}\n\nBetter"
                           f" luck next time", "Loser")

        goodbye = easygui.buttonbox("Would you like to play another round?",
                                    "Replay", ["Yes", "No"])
        if goodbye == "Yes":
            continue
        else:
            break
    else:
        number += 1
        continue
