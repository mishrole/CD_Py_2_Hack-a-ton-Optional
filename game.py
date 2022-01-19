from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.ninjaBlack import NinjaBlack
from classes.pirateBlack import PirateBlack

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")
michelangelo.attack(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow)
jack_sparrow.attack(michelangelo).attack(michelangelo).attack(michelangelo).attack(michelangelo).attack(michelangelo)
jack_sparrow.attack(michelangelo).attack(michelangelo)
jack_sparrow.show_stats()
michelangelo.show_stats()

print("--------------------------------\n")

mitchell = NinjaBlack("Mitchell")
barbanegra = PirateBlack("Barbanegra")
mitchell.stealStrength(barbanegra).stealStrength(barbanegra).attack(barbanegra).attack(barbanegra)
barbanegra.stealHealth(mitchell).stealHealth(mitchell).attack(mitchell).attack(mitchell)

mitchell.stealStrength(barbanegra)
barbanegra.stealHealth(mitchell)
mitchell.stealStrength(barbanegra)
barbanegra.stealHealth(mitchell)

mitchell.show_stats()
barbanegra.show_stats()

print("--------------------------------\n")

Ninja.printNinjasList()