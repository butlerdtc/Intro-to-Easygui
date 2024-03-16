"""Version 1 of a timer I made if ever needed
Use of online assistance for the 'for loop' only
Created by Robson Butler
"""

# Imports modules 'easygui' and 'time'
import time
import easygui

# Defines statements
timer_finished = ""
use_again = ""
# Loop to run the timer until user specifies no
while True:
    # Retains if timer has been used
    used = 0

    # While loop to check if time entered is valid
    while True:
        choose_time = easygui.integerbox("What do you want to set the timer "
                                         "to (seconds): ", "Enter Start Time",
                                         upperbound=100000)
        if choose_time > 0:
            break
        else:
            easygui.msgbox("Please enter positive value for timer", "Error")

    # Asks user if they want to start the timer
    start_timer = easygui.buttonbox("Start the timer", "Start Timer",
                                    ["Yes", "No"])
    # If yes runs the timer
    if start_timer == "Yes":
        for i in reversed(range(0, choose_time)):
            seconds = i % 60
            minutes = int(i / 60) % 60
            hours = int(i / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)

        timer_finished = easygui.buttonbox("Times Up\n\nWould you like to use "
                                           "the timer again?\n",
                                           "Timer Finished",
                                           ["Yes", "No"])
        used += 1
    else:
        use_again = easygui.buttonbox("Would you like to use the timer?",
                                      "Use Timer", ["Yes", "No"])

    # Runs the end of the program
    if timer_finished == "No" or use_again == "No":
        if used > 0:
            easygui.msgbox("Thanks for using this timer", "Goodbye")
        else:
            easygui.msgbox("Goodbye", "Goodbye")
        break
    else:
        continue
