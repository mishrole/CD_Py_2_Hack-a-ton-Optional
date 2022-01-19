from classes.pirate import Pirate

class PirateBlack(Pirate):
    def __init__( self, name ):
        super().__init__( name )
        self.strength = super().getStrength() + 10
        self.speed = super().getSpeed() + 2
        self.health = super().getHealth() + 45
    
    def stealHealth( self, ninja ):
        if not super().getIsWinner() and not ninja.getIsWinner():
            print(f"{self.name} activate special attack! \n{ninja.name} lost 2 health point")
            ninja.health -= 2
            super().attack( ninja )
        return self
