#
# This script creates a Pi Pico object and prompts the user for input
# to send the Pi Pico a custom command. This script is mostly just useful
# for testing purposes if you are adding your own custom actions in main.py.

from picocom import PiPicoCommunicator

# Check device manager under "Ports (COM & LPT)" for a USB Serial Port.
# There might be more than one, so unplug and replug your USB serial adapter
# until you know which port your serial adapter is using. Once you know
# which port it's on, change 'COM11' below to whatever your port is.

pico_communicator = PiPicoCommunicator(port='COM11')

while True:

    # Currently, there are only a few actions baked into the code:
    # rumble, ping, and crash. More can be added by modifying main.py
    # and uploading it to the Pi Pico.

    # Example usage:
    #
    # To rumble motor 1 at 50% power, you would input "rumble", "1", and "50"
    # when prompted. Motors 1, 2, 3, 4, and all are acceptable inputs for param1.

    action = input("Action: ")
    param1 = input("Parameter 1: ")
    param2 = input("Parameter 2: ")

    pico_communicator.send_message(action, param1, param2)

    print("\nSent pico {}({}, {})\n".format(action, param1, param2))