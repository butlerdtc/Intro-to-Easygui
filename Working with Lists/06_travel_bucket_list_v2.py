"""Travel Bucket list v2 """

import easygui

while True:
    places = easygui.enterbox("What are your 5 bucket list places you would "
                              "like to visit\nSeparate each place with a "
                              "comma", "Enter favourite places")
    number_places = places.split(",")
    if len(number_places) != 5:
        easygui.msgbox(f"Please enter 5 places\nYou entered "
                       f"{len(number_places)} place", "Error")
        continue
    else:
        break

result = "\n-    ".join(number_places)
easygui.msgbox(f"My bucket list places: \n\n-    {result}", "Travel "
                                                            "Bucket List")

new_places = easygui.enterbox("What place do you want to change?\nSeparate "
                              "with a comma")

change_place, new_place = new_places.split(",")
replacement_index = number_places.index(change_place.strip())
number_places[replacement_index] = new_place.strip()

second_result = "\n-    ".join(number_places)
easygui.msgbox(f"My bucket list places: \n\n-    {second_result}",
               "Travel Bucket List")
