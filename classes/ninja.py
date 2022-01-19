class Ninja:

    ninjasList = []

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.isWinner = False

        Ninja.ninjasList.append( self )
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        if not self.isWinner and not pirate.isWinner:
            if not self.isOponentExhausted( pirate ):
                pirate.health -= self.strength
                print(f"{pirate.name} took {self.strength} damage, {pirate.health} HP left\n")
                self.isOponentExhausted( pirate )
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

    def isOponentExhausted( self, pirate ):
        if pirate.health <= 0:
            print(f"{pirate.name} is exhausted. Game is over.\n🎉 {self.name} WIN 🎉\n")
            self.isWinner = True
            return True
        
        return False
    
    def getIsWinner( self ):
        return self.isWinner

    @classmethod
    def printNinjasList( cls ):
        print("Lista de Ninjas \n")
        for ninja in cls.ninjasList:
            ninja.show_stats()