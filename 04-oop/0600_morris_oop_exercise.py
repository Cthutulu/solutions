"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
."""

class Miner:
    def __init__(self):
        self.turn = 0
        self.sleepiness = 0
        self.thirst = 0
        self.hunger = 0
        self.whiskey = 0
        self.gold = 0

    def nominus(self):
        self.sleepiness = max(0, self.sleepiness)
        self.thirst = max(0, self.thirst)
        self.hunger = max(0, self.hunger)

    def death(self):
        return any (stat >= 100 for stat in [self.sleepiness, self.thirst, self.hunger])

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 5
        self.hunger += 5

    def mine(self):
        self.sleepiness += 5
        self.thirst += 10
        self.hunger += 10
        self.gold += 10

    def eat(self):
        if self.gold >= 2:
            self.sleepiness += 5
            self.thirst -= 5
            self.hunger -= 15
            self.gold -= 2

    def buy_whiskey(self):
        if self.gold >= 1:
            self.sleepiness += 5
            self.thirst += 1
            self.hunger += 1
            self.whiskey += 1
            self.gold -= 1

    def drink(self):
        if self.whiskey >= 1:
            self.sleepiness += 5
            self.thirst -= 17
            self.hunger += 1
            self.whiskey -= 1

    def rest(self):
        self.sleepiness -= 5
        self.thirst += 3
        self.hunger += 3

    def rent(self):
        self.gold -= 25


morris = Miner()


while morris.turn < 1000:
    morris.turn += 1

    # Work Days:
    if morris.turn % 7 in (1, 2, 3, 4, 5):
        if morris.sleepiness >= 60:
            morris.eat()
            morris.rest()
            morris.sleep()
        elif morris.gold < 5:
            morris.mine()
            morris.mine()
            morris.mine()
            morris.mine()
            morris.eat()
            morris.sleep()
        elif morris.gold < 10:
           morris.mine()
           morris.mine()
           morris.eat()
           morris.sleep()
        else:
            morris.mine()
            morris.eat()
            morris.sleep()

    # Wekend:
    if morris.turn % 7 in (0, 6):
        morris.eat()
        morris.buy_whiskey()
        morris.drink()
        morris.sleep()

    # Rent Day: :(
    if morris.turn % 7 in (0,):
        morris.rent()

    # For those hungry and thirsty moments:
    if morris.thirst > 60:
        while morris.thirst > 50:
            morris.buy_whiskey()
            morris.drink()

    if morris.hunger > 60:
        while morris.hunger > 40:
            morris.eat()


    if morris.death():
        print("Game Over")
        break

    morris.nominus()


    print(vars(morris))