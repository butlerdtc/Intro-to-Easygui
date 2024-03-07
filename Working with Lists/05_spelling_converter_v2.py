"""Convert NZ English Spelling to US English - Spelling Converter v1"""

import easygui

word = easygui.enterbox("Please enter word to convert", "User Word")
# Convert user input to a list
word_list = list(word)

# letters_to_remove = "u"
# position = (word.find(letters_to_remove))
# for letter in range(len(letters_to_remove)):
#     word_list.pop(position)
# word_list = ''.join(word_list)
# output = easygui.msgbox(f"Your word, {word} in American spelling is "
#                         f"{word_list}")
