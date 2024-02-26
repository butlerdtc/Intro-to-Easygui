import easygui
import random

welcome = easygui.buttonbox("Welcome to Rock, Paper, Scissors\n Rock "
                            "beats Scissors\n Scissors beats Paper\n Paper "
                            "beats Rock\n Do you want to play? ",
                            "Welcome and Rules", ["Yes", "No"])

if welcome == "Yes":
    weapon = easygui.buttonbox("Choose your weapon",
                               "Choose Weapon", ["Paper",
                                                 "Scissors", "Rock"])
    options = ["Paper", "Scissors", "Rock"]
    computer = random.choice(options)
    result = easygui.msgbox(f"You chose {weapon} and the computer chose "
                            f"{computer}")
    if weapon == computer:
        draw = easygui.msgbox("This was a draw", "Result")
    else:
        if weapon == "Paper" and computer == "Rock":
            winner = easygui.msgbox("You win", "Result")
        elif weapon == "Scissors" and computer == "Paper":
            winner = easygui.msgbox("You win", "Result")
        elif weapon == "Rock" and computer == "Scissors":
            winner = easygui.msgbox("You win", "Result")
        else:
            lost = easygui.msgbox("You lost", "Result")
easygui.msgbox("Goodbye", "Goodbye")
