#Defining GamePiece parent and child classes to use in developing game modes
class GamePiece():
    def __init__(self,name,motorPower):
        self.name = name
        self.motorPower = 0

    def __str__(self):
        return "This game pieces name is: " + self.name + "\nits motor power is: " + str(self.motorPower)
    
    def setMotorPower(pwr):
        motorPower = pwr

class AdamsApple(GamePiece):
    def __init__(self):
        super().__init__("Adam's Apple")

class BrokenHeart(GamePiece):
    def __init__(self):
        super().__init__("Broken Heart")

class WrenchedAnkle(GamePiece):
    def __init__(self):
        super().__init__("Wrenched Ankle")

class ButterfliesInStomach(GamePiece):
    def __init__(self):
        super().__init__("Butterflies in Stomach")

class SpareRibs(GamePiece):
    def __init__(self):
        super().__init__("Spare Ribs")

class WaterOnTheKnee(GamePiece):
    def __init__(self):
        super().__init__("Water on the Knee")

class FunnyBone(GamePiece):
    def __init__(self):
        super().__init__("Funny Bone")

class WritersCramp(GamePiece):
    def __init__(self):
        super().__init__("Writer's Cramp")

class CharleyHorse(GamePiece):
    def __init__(self):
        super().__init__("Charley Horse")

class AnkleBoneConnectedToTheKneeBone(GamePiece):
    def __init__(self):
        super().__init__("Ankle Bone Connected to the Knee Bone")

class WishBone(GamePiece):
    def __init__(self):
        super().__init__("Wish Bone")

class BreadBasket(GamePiece):
    def __init__(self):
        super().__init__("Bread Basket")

class BrainFreeze(GamePiece):
    def __init__(self):
        super().__init__("Brain Freeze")



    


