#
# This is a gamemode for playing a normal game of operation. Power level is adjustable by
# changing 'power_level'.

from picocom import PiPicoCommunicator

power_level = 15

pico = PiPicoCommunicator(port='COM11', debug=True)

print("Pico connected\nRegular operation game running at " + str(power_level) + "% power")

pico.rumble("all",0)

while True:
    button = pico.check_state()

    if button == 'contact':
        pico.rumble("all", power_level)
    elif button == 'no_contact':
        pico.rumble("all", 0)