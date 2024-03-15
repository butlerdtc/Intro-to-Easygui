import time
import easygui

while True:
    choose_time = easygui.integerbox("What time to set the timer to "
                                     "(seconds): ", "Enter Start Time",
                                     upperbound=100000)
    if choose_time > 0:
        break
    else:
        easygui.msgbox("Please enter positive value for timer", "Error")

start_timer = easygui.buttonbox()

for i in reversed(range(0, choose_time)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times up!")
