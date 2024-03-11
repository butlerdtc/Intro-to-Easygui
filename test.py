import easygui
import random

number = random.randint(0, 5)
print(number)

words = ["bat", "cat", "sat", "pat"]
# my_word = random.choice(words)
# print(my_word)
#
# friend = "Rafael"
# letter = random.choice(friend)
# print(letter)
#
# welcome = easygui.msgbox("Welcome to Easygui", "Welcome")
#
# name = easygui.enterbox("Hi, Whats your name? ", "Name")
# print(name)
#
# age = easygui.integerbox("How old are you? ")
# print(age)
#
# last_name = easygui.buttonbox("Choose gender", "Gender",
#                               ["Male", "Female", "Other"])
#
# carry_on = easygui.buttonbox("Do you want to continue?",
#                              choices=["Yes", "No", "Don't care"],
#                              title="Continue")
list_1 = ["Monkey"]
list_2 = list_1[-1::2]
print(list_2)

words.sort(reverse=True)
print(words)
