import easygui
import random

count = 0
word = "elephant"

while count < 5:
    count += 1
    letter = random.choice(word)
    easygui.msgbox(f"{letter}", f"Letter {count} chosen")
