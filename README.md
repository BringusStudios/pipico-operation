# pipico-operation

This is the repo for everything about the Operation game I created on my YouTube channel Bringus Studios: https://www.youtube.com/@BringusStudios

This code is VERY unprofessionally made, and it can feel unresponsive sometimes, and straight up just misbehave. I did my Bringus Best but at the end of the day it is spaghetti code, and there will be bugs. I am not responsible if you burn your house or loved ones down trying to make your own copy of the game. I will provide assistance when I can, but it will be infrequent if at all.

All of the code is available across the various .py files: 

- main.py is the code that runs on the Pico itself
- picocom.py is the library that handles serial communication between the pico and a PC
- buttonstate.py is example code that detects when the user has made contact with the object chambers
- commander.py is a debugging tool that can send custom commands to the Pi in case you make changes to main.py to add your own actions
- inc_on_space.py is gamemode 1 from the video
- time_attack.py is gamemode 2 from the video
- regular_game.py makes the game behave like a normal game of operation

The .f3d file is the Fusion 360 project file with all the 3D printed parts. I used M3 brass inserts and various length M3 screws to bolt things down, and hot glue to attach the walls/legs and electronics mounts. The Pico needs some itty bitty screws that I have no idea the size of.

As for wiring it all up... you're on your own. Look through main.py to get an idea of what gpio pins everything should be connected to. The tweezers need to be wired with a pullup resistor to 3.3v, and the ground plane of the game needs to be grounded. Making everything else work, like the DC motors, motor controller, serial adapter, etc., is all you.
