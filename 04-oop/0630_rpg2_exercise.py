"""opgave: Objektorienteret rollespil, afsnit 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af afsnit 1.

Del 1:
    Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
    Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
    Måske overskriver de også metoder eller attributter fra klassen Character.

Del 2:
    Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
    indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Del 3:
    Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Del 4:
    Lad dine figurer kæmpe mod hinanden 100 gange.
    Hold styr på resultaterne.
    Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import random

class Character:
    def __init__(self, name: str, health: int, p_attack: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int):
        self.name = name
        self.max_health = health
        self._current_health = health
        self.p_attack = p_attack
        self.m_attack = m_attack
        self.phy_defense = phy_defense
        self.mag_defense = mag_defense
        self.speed = speed

    def __repr__(self):
        return f"{self.name} has {self._current_health}/{self.max_health} health"

    def phy_attack(self, other):
        if self.is_alive():
            damage = self.p_attack
            crit = random.random() < 0.10
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} magic damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_p_damage(self.p_attack)
        # else:             # for testing
        #     print(f"{self.name} is dead")

    def mag_attack(self, other):
        if self.is_alive():
            print(f"{self.name} hit {other.name} for {self.m_attack} damage")
            other._take_m_damage(self.m_attack)
        # else:             # for testing
        #     print(f"{self.name} is dead")

    def _take_p_damage(self, p_attack):
        if self.is_alive():
            damage = round(p_attack * (1 - self.phy_defense / 100))
            self._current_health -= damage
            if self._current_health <= 0:
                print(f"{self.name} has been defeated")

    def _take_m_damage(self, m_attack):
        if self.is_alive():
            damage = round(m_attack * (1 - self.mag_defense / 100))
            self._current_health -= damage
            if self._current_health <= 0:
                print(f"{self.name} has been defeated")

    def _get_healed(self, m_attack):
        self._current_health += m_attack

    def is_alive(self):
        return self._current_health > 0

    def prio_target(self, other):
        pass




class Paladin(Character):
    def __init__(self, name: str, health: int, p_attack: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, m_attack, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Paladin has {self._current_health}/{self.max_health} health"

    def heal(self, other):
        other._get_healed(int(self.m_attack / 2.5))




class Rouge(Character):
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Rouge has {self._current_health}/{self.max_health} health"




class Mage(Character):
    def __init__(self, name: str, health: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, 0, m_attack, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Mage has {self._current_health}/{self.max_health} health"




class Barbarian(Character):
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Barbarian has {self._current_health}/{self.max_health} health"




class Ranger(Character):
    def __init__(self, name: str, health: int, p_attack: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, m_attack, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Ranger has {self._current_health}/{self.max_health} health"




class Bard(Character):
    def __init__(self, name: str, health: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, 0, m_attack, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Bard has {self._current_health}/{self.max_health} health"

    def heal(self, other):
        other._get_healed(int(self.m_attack / 3))



class Warrior(Character):
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Warrior has {self._current_health}/{self.max_health} health"



class Tank(Character):
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Tank has {self._current_health}/{self.max_health} health"



class Priest(Character):
    def __init__(self, name: str, health: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, 0, m_attack, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Priest has {self._current_health}/{self.max_health} health"

    def heal(self, other):
        other._get_healed(int(self.m_attack / 2))



paladin = Paladin ("Caelvaris", 180, 15, 20, 20, 20, 5)
rouge = Rouge ("Nightshade", 90, 30, 7, 5, 30)
mage = Mage ("Merlin", 90, 30, 5, 15, 15)
barbarian = Barbarian ("Bonebreaker", 150, 25, 18, 10, 20)
ranger = Ranger ("Strider", 70, 30, 30, 5, 8, 20)
bard = Bard ("Songweaver", 80, 30, 8, 13, 18)
warrior = Warrior ("Ironfist", 130, 22, 15, 12, 22)
tank = Tank ("Sentinel", 250, 10, 35, 25, 2)
priest = Priest ("Gideon", 80, 30, 7, 13, 15)

# all_characters = [paladin, rouge, mage, barbarian, ranger, bard, warrior, tank, priest]
#
# random.shuffle(all_characters)
#
# team1 = all_characters[:3]
# team2 = all_characters[3:6]
#
# print("Team 1:")
# for char in team1:
#     print(char)
# print()
# print("Team 2:")
# for char in team2:
#     print(char)
# print()

test1 = Character("1",100, 100, 20, 5, 20, 10)
test2 = Character("2",100, 100, 20, 5, 20, 10)

print(test1)
print(test2)

test1.mag_attack(test2)
test2.mag_attack(test1)

print(test1)
print(test2)

"""
random damage rolls, and a change for double damage (crit)
different special moves for each class
teams of 3 against each other     =Done
1 team win when the other team has no health
random move choice, BUT with some things being a higher change fx, if an attack can kill it has higher change, and if you have low health the higher change for protecting, and if an ally has little health higher change to heal
move order by speed stat
cannot do anything when no health
"""
