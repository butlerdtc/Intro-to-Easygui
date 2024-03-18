import easygui

hero_0 = {"Name": "Materdon",
          "Power": "Flight",
          "Strength": 5}

if "Name" in hero_0:
    easygui.msgbox(f"The heroes name is {hero_0["Name"]}")
else:
    easygui.msgbox("There is no superhero")
if "Speed" in hero_0:
    easygui.msgbox(f"The heroes speed is {hero_0["Speed"]}")
else:
    easygui.msgbox("There is no superhero speed")
