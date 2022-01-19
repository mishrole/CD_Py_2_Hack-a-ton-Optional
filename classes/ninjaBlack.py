from classes.ninja import Ninja

class NinjaBlack( Ninja ):
    def __init__( self, name ):
        super().__init__( name )
        self.strength = super().getStrength() + 15
        self.speed = super().getSpeed() + 3
        self.health = super().getHealth() + 50
    
    def stealStrength( self, pirate ):
        if not super().getIsWinner() and not pirate.getIsWinner():
            print(f"{self.name} activate special attack! \n{pirate.name} lost 1 stregth point")
            pirate.strength -= 1
            super().attack( pirate )
        return self