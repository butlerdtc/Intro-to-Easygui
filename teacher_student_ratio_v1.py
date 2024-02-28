import easygui

name = easygui.enterbox("Enter the name of the school", "School "
                                                        "Name")
max_class_size = easygui.integerbox("What is the maximum number of "
                                    "children allowed per class:\nMust be "
                                    "between 10 and 30", "Maximum Class "
                                                         "Size",
                                    lowerbound=10, upperbound=30)
total_children = easygui.integerbox(f"What is the total number of "
                                    f"children "
                                    f"at {name} \nMust be between 10 and 1400",
                                    "Total Students", upperbound=1400,
                                    lowerbound=10)
