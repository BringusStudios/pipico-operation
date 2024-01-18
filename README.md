# pipico-operation

This is the repo for everything about the Operation game I created on my YouTube channel Bringus Studios.

I am not responsible if you burn your house or loved ones down trying to make your own copy of the game. I will provide assistance when I can, but it will be infrequent if at all.

All of the code is available across the various .py files: 

- main.py is the code that runs on the Pico itself
- picocom.py is the library that handles serial communication between the pico and a PC
- buttonstate.py is example code that detects when the user has made contact with the object chambers
- commander.py is a debugging tool that can send custom commands to the Pi in case you make changes to main.py to add your own actions
- inc_on_space.py is gamemode 1 from the video
- time_attack.py is gamemode 2 from the video
- regular_game.py makes the game behave like a normal game of operation

The .f3d file is the Fusion 360 project file with all the 3D printed parts.

As for wiring it all up... you're on your own. Look through main.py to get an idea of what gpio pins everything should be connected to. Making everything else work, like the DC motors, motor controller, serial adapter, etc., is all you.
