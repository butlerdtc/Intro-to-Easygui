"""Program to check if tech free goal has been achieved """

import easygui
days = easygui.enterbox("Please enter the days you used technology\nSeparate "
                        "them with a space", "Days Used")
day_list = days.split(" ")
count = len(day_list)
if count > 4:
    easygui.msgbox(f"You did not achieve your goal of 3 tech-free days\n"
                   f"You had {7 - count} tech free days", "Unlucky")
else:
    easygui.msgbox(f"Congratulations, You did achieve your goal of 3 "
                   f"tech-free days\nYou had {7 - count} tech free days "
                   f"this week", "Congratulations")
