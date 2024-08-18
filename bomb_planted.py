"""
It's just another average day in the ER, your fresh out of your Residency and ready to really make a difference in the medical field
In comes a patient at breakneck speed, police following suit, you ask the officer leading the rest what the situation is.


Someone, You have no clue who, you have no clue why
Has planted an actual fucking bomb in this guy disguised amongst 13 multiple cheap plastic game pieces to the game "Operation"

God Help You

-In this game mode all of the pieces will be randomized
-All of them will be set to 0 rumble power... Except 1, which will be set to 100%, hitting that piece will make the game rumble for 3 seconds
-The game will print a list of all the pieces, select the one you will be attempting to remove and then perform the operation
-Press space when youve finished removing the item and keep going
- You win by removing all but the "Bomb"

Choose wisely
"""
from GamePieces import *
from picocom import PiPicoCommunicator
import random
import keyboard
import time


GamePieceArr = create_game_pieces() #create an array of all the Operation game pieces that inherit from GamePieces
random.choice(GamePieceArr).setMotorPower(100) #Randomly select one game piece in the array to plant the "bomb"



pico = PiPicoCommunicator(port='COM11', debug=True)


pico.rumble("all",0)

while True:
    result = ""
    for index, gamepieces in enumerate(GamePieceArr):
        result += f"Index {index}: {gamepieces.name}\n" #create display list to print pieces that have not been attempted yet
    
    print("Choose the piece you will be working on")
    choice = int(input()) #input() is program blocking but you shouldnt be touching the game at this point anyways

    try: #try except statement to catch invalid index
        power_level = GamePieceArr[choice].motorPower
    except(TypeError, IndexError):
        print("Please input an integer correlating with the index's of the game pieces!")

    print(f"You've selected {GamePieceArr[choice].name} good luck doctor, press space when you've removed the piece")
    #Player is now expected to be working on a game piece

    if keyboard.is_pressed('space'):
        print("Good job doctor!")
        GamePieceArr.pop(choice) #removes game piece from array to mark as "completed"
    
    if len(GamePieceArr) == 1: #Breaks from loop once you have removed all pieces except for the bomb
        print(f"Congrats doctor you've done it, the bomb was the {GamePieceArr[choice].name}")
        break
    
    #pico enabling code
    button = pico.check_state()

    if button == 'contact':
        if GamePieceArr[choice].motorPower == 100:
            print("BOOM!")
            end_time = time.time() + 3
            while time.time() < end_time:
                pico.rumble("all", power_level)
                time.sleep(1)
            
        else: pico.rumble("all", power_level)

    elif button == 'no_contact':
        pico.rumble("all", 0)
