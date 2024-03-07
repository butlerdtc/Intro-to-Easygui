"""Convert NZ English Spelling to US English - Spelling Converter v1"""

import easygui

while True:
    word = easygui.enterbox("Please enter word to convert", "User Word")
    # Retains original word
    original_word = word

    if "ise" in word:
        new_word = word.replace("ise", "ize")
        easygui.msgbox(f"You entered {original_word}, and its american "
                       f"spelling is {new_word}")
    elif "yse" in word:
        new_word = word.replace("yse", "yze")
        easygui.msgbox(f"You entered {original_word}, and its american "
                       f"spelling is {new_word}")
    elif "our" in word:
        new_word = word.replace("our", "or")
        easygui.msgbox(f"You entered {original_word}, and its american "
                       f"spelling is {new_word}")
    else:
        easygui.msgbox("No spelling changes needed", "No changes")
    run_again = easygui.buttonbox("Would you like to convert another word:",
                                  "Run program again", ["Yes", "No"])
    if run_again == "Yes":
        continue
    else:
        break
thanks = easygui.msgbox("Thanks for using our program", "Thank you")
