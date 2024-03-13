"""Yahtzee Lite v1"""

import easygui
import random

dice = ["1", "2", "3", "4", "5", "6"]
number = 0
while True:
    result = []
    for i in range(5):
        rolled = random.choice(dice)
        result.append(rolled)
    result.sort()
    final_result = ", ".join(result)
    sequence = easygui.buttonbox(f"You have rolled: {final_result}\n\n"
                                 f"Choose:", "Result",
                                 ["Roll again", "Stick"])
    if sequence == "Stick" or number == 2:
        for item in result:
            if item == result[item]:
                
    else:
        number += 1
        continue
