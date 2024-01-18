#
# This script creates a Pi Pico object and prompts the user for
# inputs to control individual motors. 

import time
from picocom import PiPicoCommunicator

# Check device manager under "Ports (COM & LPT)" for a USB Serial Port.
# There might be more than one, so unplug and replug your USB serial adapter
# until you know which port your serial adapter is using. Once you know
# which port it's on, change 'COM11' below to whatever your port is.

pico_communicator = PiPicoCommunicator(port='COM11')

while True:

    motor = input("Which motor: ")
    pwr = input("How hard: ")
    duration = input("How long: ")

    pico_communicator.rumble(motor, pwr)
    time.sleep(int(duration))
    pico_communicator.rumble(motor, 0)