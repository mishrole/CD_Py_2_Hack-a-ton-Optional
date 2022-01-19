class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.isWinner = False

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , ninja ):
        if not self.isWinner and not ninja.isWinner:
            if not self.isOponentExhausted( ninja ):
                ninja.health -= self.strength
                print(f"{ninja.name} took {self.strength} damage, {ninja.health} HP left\n")
                self.isOponentExhausted( ninja )
            else:
                print(f"Oops {self.name}. This game is over")

        return self

    def getName( self ):
        return self.name

    def getStrength( self ):
        return self.strength

    def getSpeed( self ):
        return self.speed
    
    def getHealth( self ):
        return self.health

    def isOponentExhausted(self, ninja ):
        if ninja.health <= 0:
            print(f"{ninja.name} is exhausted. Game is over.\n🎉 {self.name} WIN 🎉\n")
            self.isWinner = True
            return True

        return False

    def getIsWinner( self ):
        return self.isWinner

