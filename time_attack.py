#
# This is the code for the 2nd gamemode featured at the end of the video.
# Sometimes it crashes when trying to play the sound file. No idea why.

import time
import keyboard
from picocom import PiPicoCommunicator
from playsound import playsound

pico = PiPicoCommunicator(port='COM11', debug=False)

print("Pico connected\n\nPress space to begin\n")

pico.rumble("all", 0)

def start_game():
    print("Time attack started")
    playsound('audio.mp3')
    start_time = time.time()

    power_level = 10
    interval = 1 #seconds
    time_limit = 60 #seconds
    increment = 5 #seconds

    power_increment = (100-power_level)/((time_limit/increment)-1)
    current_count = 0

    while time_limit > 0:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= interval:
            time_limit = time_limit - 1
            print(time_limit)
            start_time = time.time()
            current_count = current_count + 1

        if current_count >= increment and time_limit > 0:
            power_level = power_level + power_increment
            print("CRANKING IT TO " + str(power_level) + "%")
            playsound('audio.mp3')
            current_count = 0

        button = pico.check_state()

        if button == 'contact':
            pico.rumble("all", power_level)
        elif button == 'no_contact':
            pico.rumble("all", 0)

    print("\nThanks for playing ya big dummy. Press space to play again.\n")

while True:
    time.sleep(0.1)

    if keyboard.is_pressed('space'):
        start_game()
