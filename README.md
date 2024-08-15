# pipico-operation

This is the repo for everything about the Operation game I created on my YouTube channel Bringus Studios: https://www.youtube.com/@BringusStudios

This code is VERY unprofessionally made, and the game can feel weird and unresponsive sometimes because of it, and sometimes it just straight up misbehaves. I did my Bringus Best, but at the end of the day it's spaghetti code, and there will be bugs. I am not responsible if you burn your house or loved ones down trying to make your own copy of the game. I will provide assistance when I can, but it will be infrequent if at all.


All of the code is available across the various .py files:
Please pip install pyserial as it is needed to run the code
- main.py is the code that runs on the Pico itself
- picocom.py is the library that handles serial communication between the pico and a PC
- buttonstate.py is example code that detects when the user has made contact with the object chambers
- commander.py is a debugging tool that can send custom commands to the Pi in case you make changes to main.py to add your own actions
- inc_on_space.py is gamemode 1 from the video
- time_attack.py is gamemode 2 from the video
- regular_game.py makes the game behave like a normal game of operation

The .f3d file is the Fusion 360 project file with all the 3D printed parts. I used M3 brass inserts and various length M3 screws to bolt things down, and hot glue to attach the walls/legs and electronics mounts. The Pico needs some itty bitty screws that I have no idea the size of.

As for wiring it all up... you're on your own. Look through main.py to get an idea of what gpio pins everything should be connected to. The tweezers need to be wired with a pullup resistor to 3.3v, and the ground plane of the game needs to be grounded. Making everything else work, like the DC motors, motor controller, serial adapter, etc., is all you.

Misc links to the parts I used to build it:

- https://www.walmart.com/ip/Classic-Family-Favorite-Operation-Game-Board-Game-for-Kids-and-Family-Ages-6-and-Up/51404444
- https://www.amazon.com/dp/B0C5JCF5RS
- https://www.amazon.com/dp/B01N1GAWQ5
- https://www.amazon.com/dp/B089KRYQ5P
- https://www.amazon.com/dp/B0B4VWZD7X
- https://www.amazon.com/dp/B07BS8SRWH
- https://www.amazon.com/dp/B07WX2DSVB
- https://www.amazon.com/dp/B091PS6XQ4
- https://www.amazon.com/dp/B08C594VNP
- https://www.amazon.com/KEYESTUDIO-Raspberry-Starter-Headers-Breadboard/dp/B0861WJ2DD/



