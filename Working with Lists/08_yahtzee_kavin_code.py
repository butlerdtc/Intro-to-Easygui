import easygui
import random

dice = ["1", "2", "3", "4", "5", "6"]
rolled_list_player1 = []
rolled_list_player2 = []
player1 = easygui.enterbox(title="PLayer 1 Name", msg="Player 1, enter your "
                                                      "name:")
player2 = easygui.enterbox(title="Player 2 Name", msg="Player 2, enter your "
                                                      "name:")

while True:
    turns_player1 = 1
    turns_player2 = 1
    for rolled_player1 in dice:
        dice1_rolled = random.choice(dice)
        dice2_rolled = random.choice(dice)
        dice3_rolled = random.choice(dice)
        dice4_rolled = random.choice(dice)
        dice5_rolled = random.choice(dice)

        rolled_list_player1 = [dice1_rolled, dice2_rolled, dice3_rolled,
                               dice4_rolled, dice5_rolled]
        roll_again = easygui.buttonbox(msg=f"{player1} rolled: {dice1_rolled},"
                                           f" {dice2_rolled}, {dice3_rolled}, "
                                           f"{dice4_rolled}, "
                                           f"{dice5_rolled}.\n\nChoose:",
                                       choices=["Roll again", "Stick"])
        if turns_player1 == 3:
            easygui.msgbox(title="No more turns", msg="You've used all three "
                                                      "turns!")
            break
        elif roll_again == "Stick":
            break
        elif roll_again == "Roll again":
            turns_player1 += 1

    player1_points = 0

    rolled_list_player1.sort()
    if rolled_list_player1[0] == rolled_list_player1[4]:
        easygui.msgbox(title="Yahtzee!", msg="Yahtzee! 50 points awarded.")
        player1_points += 50
    elif (rolled_list_player1[0] == rolled_list_player1[3] or
          rolled_list_player1[1] == rolled_list_player1[4]):
        easygui.msgbox(title="4 of a Kind!", msg="4 of a kind! 30 points "
                                                 "awarded.")
        player1_points += 30
    elif (rolled_list_player1[0] == rolled_list_player1[2] or
          rolled_list_player1[1] == rolled_list_player1[3] or
          rolled_list_player1[2] == rolled_list_player1[4]):
        easygui.msgbox(title="3 of a Kind!", msg="3 of a kind! 10 points "
                                                 "awarded.")
        player1_points += 10
    else:
        easygui.msgbox(title="You lose.", msg="No points awarded, better luck "
                                              "next time.")

    for rolled_player2 in dice:
        dice1_rolled = random.choice(dice)
        dice2_rolled = random.choice(dice)
        dice3_rolled = random.choice(dice)
        dice4_rolled = random.choice(dice)
        dice5_rolled = random.choice(dice)

        rolled_list_player2 = [dice1_rolled, dice2_rolled, dice3_rolled,
                               dice4_rolled, dice5_rolled]
        roll_again = easygui.buttonbox(msg=f"{player2} rolled: "
                                           f"{dice1_rolled}, {dice2_rolled}, "
                                           f"{dice3_rolled}, "
                                           f"{dice4_rolled}, "
                                           f"{dice5_rolled}.\n\nChoose:",
                                       choices=["Roll again", "Stick"])
        if turns_player2 == 3:
            easygui.msgbox(title="No more turns", msg="You've used all three "
                                                      "turns!")
            break
        elif roll_again == "Stick":
            break
        elif roll_again == "Roll again":
            turns_player2 += 1

    player2_points = 0
    rolled_list_player2.sort()
    if rolled_list_player2[0] == rolled_list_player2[4]:
        easygui.msgbox(title="Yahtzee!", msg="Yahtzee! 50 points awarded.")
        player2_points += 50
    elif (rolled_list_player2[0] == rolled_list_player2[3] or
          rolled_list_player2[1] == rolled_list_player2[4]):
        easygui.msgbox(title="4 of a Kind!", msg="4 of a kind! 30 points "
                                                 "awarded.")
        player2_points += 30
    elif (rolled_list_player2[0] == rolled_list_player2[2] or
          rolled_list_player2[1] == rolled_list_player2[3] or
          rolled_list_player2[2] == rolled_list_player2[4]):
        easygui.msgbox(title="3 of a Kind!", msg="3 of a kind! 10 points "
                                                 "awarded.")
        player2_points += 10
    else:
        easygui.msgbox(title="You lose.", msg="No points awarded, better "
                                              "luck next time.")

    if player1_points > player2_points:
        easygui.msgbox(title=f"{player1} Wins!", msg=f"{player1} wins with "
                                                     f"{player1_points} "
                                                     f"points!\n"
                                                     f"{player2} lost with "
                                                     f"{player2_points} "
                                                     f"points.")
    elif player1_points < player2_points:
        easygui.msgbox(title=f"{player2} Wins!", msg=f"{player2} wins with "
                                                     f"{player2_points} "
                                                     f"points!\n"
                                                     f"{player1} lost with "
                                                     f"{player1_points} "
                                                     f"points.")
    else:
        easygui.msgbox(title="Tie!", msg=f"{player1} and {player2} tied with "
                                         f"{player1_points} points!")

    play_again = easygui.buttonbox(title="Play again?", msg="Do you want to "
                                                            "play again or "
                                                            "quit?",
                                   choices=["Play again", "Quit"])
    if play_again == "Quit":
        break
