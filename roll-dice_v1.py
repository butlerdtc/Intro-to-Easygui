import easygui
import random

player = 0

for roll in range(2):
    player += 1
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    easygui.msgbox(f"Player {player} rolled:\n\n {die1} and {die2}\n\n"
                   f"Total: {total}", f"{player}")
