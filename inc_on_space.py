#
# This is the code for the 1st gamemode featured at the end of the video.

import time
import keyboard
from picocom import PiPicoCommunicator

initial_level = 10
increment = 7.5
power_level = initial_level

pico = PiPicoCommunicator(port='COM11', debug=False)

print("Pico connected\nIncreasing power level by " + str(increment) + "% upon spacebar press and starting at " + str(initial_level) + "% power\n\n\n")

pico.rumble("all", 0)

def feedback():
    i = 3
    while i > 0:
        pico.rumble("all", 20)
        time.sleep(0.05)
        pico.rumble("all", 0)
        time.sleep(0.05)
        i -= 1

while True:
    if keyboard.is_pressed('space'):
        if power_level == 100:
            power_level = 10
            print("Power level reset to", power_level, "%")
        else:
            power_level += increment
            print("Power level increased to", power_level, "%")
        feedback()

    button = pico.check_state()

    if button == 'contact':
        pico.rumble("all", power_level)
    elif button == 'no_contact':
        pico.rumble("all", 0)