import easygui

while True:
    name = easygui.enterbox("Enter the name of the school", "School "
                            "Name")
    max_class_size = easygui.integerbox("What is the maximum number of "
                                        "children allowed per class:\nMust be "
                                        "between 10 and 30", "Maximum "
                                                             "Class Size",
                                        lowerbound=10, upperbound=30)
    total_children = easygui.integerbox(f"What is the total number of "
                                        f"children "
                                        f"at {name} \nMust be between 10 and "
                                        f"1400", "Total Students",
                                        upperbound=1400, lowerbound=10)

    number_classes = total_children // max_class_size
    if total_children % max_class_size > 0:
        number_classes += 1
    total_teachers = easygui.integerbox(f"What is the total number of "
                                        f"teachers"
                                        f" at {name} \nMust be between 1 and "
                                        f"120", "Total Teachers",
                                        upperbound=120, lowerbound=1)

    if total_teachers == number_classes:
        easygui.msgbox("You have the correct number of teachers",
                       "Staff Result")
    elif total_teachers > number_classes:
        easygui.msgbox(f"You have too many teachers\n\nYou could do "
                       f"without {total_teachers - number_classes} teachers",
                       "Staff Result")
    else:
        easygui.msgbox(f"You have too few teachers\n\nYou could do "
                       f"with {number_classes - total_teachers} more teachers",
                       "Staff Result")
    redo = easygui.buttonbox("Do you want to perform another calculation",
                             "Run again", ["Yes", "No"])
    if redo == "Yes":
        continue
    else:
        easygui.msgbox("Thank you for using this program",
                       "Goodbye",)
        break
