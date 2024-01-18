#
# This script creates a Pi Pico object and monitors for 'button presses'
# in the form of the user touching the walls of the object chambers.

from picocom import PiPicoCommunicator

# Check device manager under "Ports (COM & LPT)" for a USB Serial Port.
# There might be more than one, so unplug and replug your USB serial adapter
# until you know which port your serial adapter is using. Once you know
# which port it's on, change 'COM11' below to whatever your port is.

pico_communicator = PiPicoCommunicator(port='COM11')

print("Monitoring button state...")

while True:
    state_change = pico_communicator.check_state()
            
    if state_change:
        print(f"State changed to '{state_change}'")