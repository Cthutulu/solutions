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
            crit = random.random() < 0.05
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_p_damage(damage)

    def mag_attack(self, other):
        if self.is_alive():
            damage = self.m_attack
            crit = random.random() < 0.05
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_m_damage(damage)

    def _take_p_damage(self, p_attack):
        if self.is_alive():
            damage = round(p_attack * (1 - self.phy_defense / 100))
            self._current_health -= damage
            print(f"{self.name} takes {damage} damage")
            if self._current_health <= 0:
                print(f"{self.name} has been defeated")

    def _take_m_damage(self, m_attack):
        if self.is_alive():
            damage = round(m_attack * (1 - self.mag_defense / 100))
            self._current_health -= damage
            print(f"{self.name} takes {damage} damage")
            if self._current_health <= 0:
                print(f"{self.name} has been defeated")

    def _get_healed(self, amount):
        self._current_health = min(self._current_health + amount, self.max_health)

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

    def radiant_strike(self, other):
        if self.is_alive():
            damage = self.m_attack
            crit = random.random() < 0.10
            if crit:
                damage *= 2.2
            variation = random.uniform(1.45, 1.55)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_m_damage(damage)

    def sacred_slash(self, other):
        if self.is_alive():
            damage = self.p_attack
            crit = random.random() < 0.05
            if crit:
                damage *= 2.1
            variation = random.uniform(1.25, 1.35)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_p_damage(damage)

    def normal_attack(self, other):
        if self.is_alive():
            damage = self.p_attack
            crit = random.random() < 0.05
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_p_damage(damage)




class Rogue(Character):
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed)
        self.untargetable = False
        self.untargetable_turns = 0

    def __repr__(self):
        return f"{self.name} the Rouge has {self._current_health}/{self.max_health} health"

    def sacred_slash(self, other):
        if self.is_alive():
            damage = self.p_attack
            crit = random.random() < 1.00
            if crit:
                damage *= 1.6
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            other._take_p_damage(damage)

    def vanish(self, turns=2):
        self.untargetable = True
        self.untargetable_turns = turns
        print(f"{self.name} casts Vanish and cannot be targeted for {turns} turns!")

    def normal_attack(self, other):
        if self.is_alive():
            damage = self.p_attack
            crit = random.random() < 0.05
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_p_damage(damage)


class Mage(Character):
    def __init__(self, name: str, health: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, 0, m_attack, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Mage has {self._current_health}/{self.max_health} health"

    # def chain_lightning(self, other):    hits multiple targets for little damage

    # def mana_burst(self, other):   strong attack but unable to attack next turn

    def normal_attack(self, other):
        if self.is_alive():
            damage = self.m_attack
            crit = random.random() < 0.05
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_m_damage(damage)



class Barbarian(Character):
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Barbarian has {self._current_health}/{self.max_health} health"

    # def bloodrage(self, other):            gain health on kill
    # def beserk(self):                      +damage -defense

    def normal_attack(self, other):
        if self.is_alive():
            damage = self.p_attack
            crit = random.random() < 0.05
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_p_damage(damage)



class Ranger(Character):
    def __init__(self, name: str, health: int, p_attack: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, m_attack, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Ranger has {self._current_health}/{self.max_health} health"

    # def rain_of_arrows():     hits multiple enemies for small damage physical

    def spirit_arrow(self, other):
        if self.is_alive():
            damage = self.m_attack
            crit = random.random() < 0.3
            if crit:
                damage *= 2.3
            variation = random.uniform(1.35, 1.55)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_m_damage(damage)

    def normal_attack(self, other):
        if self.is_alive():
            damage = self.p_attack
            crit = random.random() < 0.05
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_p_damage(damage)


class Bard(Character):
    def __init__(self, name: str, health: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, 0, m_attack, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Bard has {self._current_health}/{self.max_health} health"

    def heal(self, other):
        other._get_healed(int(self.m_attack / 3))

    # def hymn_of_haste():     give speed

    # def hymn_of_aegis():     give defenses

    def normal_attack(self, other):
        if self.is_alive():
            damage = self.m_attack
            crit = random.random() < 0.10
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_m_damage(damage)




class Warrior(Character):
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Warrior has {self._current_health}/{self.max_health} health"

    # def shield_bash():     stuns enemy for 1 turn

    def mighty_strike(self, other):
        if self.is_alive():
            damage = self.p_attack
            crit = random.random() < 0.05
            if crit:
                damage *= 2.5
            variation = random.uniform(1.55, 1.75)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_p_damage(damage)

    def normal_attack(self, other):
        if self.is_alive():
            damage = self.p_attack
            crit = random.random() < 0.05
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_p_damage(damage)



class Tank(Character):
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed)

    def __repr__(self):
        return f"{self.name} the Tank has {self._current_health}/{self.max_health} health"

    # def fortify():    buff defenses

    # def taunt():      become target

    def normal_attack(self, other):
        if self.is_alive():
            damage = self.p_attack
            crit = random.random() < 0.05
            if crit:
                damage *= 2
            variation = random.uniform(0.95, 1.05)
            damage *= variation
            damage = round(damage)
            print(f"{self.name} attacks {other.name} for {damage} damage", end="")
            if crit:
                print("(CRITICAL HIT!)")
            else:
                print()
            other._take_p_damage(damage)


class Priest(Character):
    def __init__(self, name: str, health: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int):
        super().__init__(name, health, 0, m_attack, phy_defense, mag_defense, speed)
        self.untargetable = False
        self.untargetable_turns = 0

    def __repr__(self):
        return f"{self.name} the Priest has {self._current_health}/{self.max_health} health"

    def normal_attack(self, other):
        other._get_healed(int(self.m_attack / 2))

    def mass_heal(self, other):     #maybe not working as you want
        other._get_healed(int(self.m_attack / 2.5))
        other._get_healed(int(self.m_attack / 2.5))
        self._get_healed(int(self.m_attack / 2.5))

    # heal all allies for small amount

    def divine_shield(self, turns=3):
        self.untargetable = True
        self.untargetable_turns = turns
        print(f"{self.name} casts Divine Shield and cannot be targeted for {turns} turns!")


paladin = Paladin ("Caelvaris", 180, 15, 20, 30, 30, 5)
rogue = Rogue ("Nightshade", 90, 30, 15, 10, 30)
mage = Mage ("Merlin", 90, 30, 10, 25, 15)
barbarian = Barbarian ("Bonebreaker", 150, 25, 25, 15, 20)
ranger = Ranger ("Strider", 70, 30, 30, 15, 15, 20)
bard = Bard ("Songweaver", 80, 30, 12, 25, 18)
warrior = Warrior ("Ironfist", 130, 22, 25, 18, 22)
tank = Tank ("Sentinel", 250, 10, 45, 35, 2)
priest = Priest ("Gideon", 80, 30, 15, 20, 15)

all_characters = [paladin, rogue, mage, barbarian, ranger, bard, warrior, tank, priest]

random.shuffle(all_characters)

team1 = all_characters[:3]
team2 = all_characters[3:6]

def random_target(enemies):
    alive = [e for e in enemies if e.is_alive()]
    if not alive:
        return None

    targetable = [e for e in alive if not getattr(e, "untargetable", False)]
    if targetable:
        return random.choice(targetable)
    else:
        return random.choice(alive)



print("Team 1:")
for char in team1:
    print(char)
print()

print("Team 2:")
for char in team2:
    print(char)
print()

def battle(team1, team2):
    round_num = 1

    while any(char.is_alive() for char in team1) and \
            any(char.is_alive() for char in team2):

        print(f"\n===== ROUND {round_num} =====\n")

        for char in team1:
            if char.is_alive():
                target = random_target(team2)
                if target:
                    char.normal_attack(target)

            if getattr(char, "untargetable", False):
                char.untargetable_turns -= 1
                if char.untargetable_turns <= 0:
                    char.untargetable = False
                    char.untargetable_turns = 0
                    print(f"{char.name} is now targetable again.")

        for char in team2:
            if char.is_alive():
                target = random_target(team1)
                if target:
                    char.normal_attack(target)

            if getattr(char, "untargetable", False):
                char.untargetable_turns -= 1
                if char.untargetable_turns <= 0:
                    char.untargetable = False
                    char.untargetable_turns = 0
                    print(f"{char.name} is now targetable again.")

        round_num += 1

    if any(char.is_alive() for char in team1):
        print("\n\nTEAM 1 WINS!")
    else:
        print("\n\nTEAM 2 WINS!")

battle(team1, team2)


# test1 = Character("1",100, 100, 20, 5, 20, 10)
# test2 = Character("2",100, 100, 20, 5, 20, 10)
#
# print(test1)
# print(test2)
#
# test1.mag_attack(test2)
# test2.mag_attack(test1)
#
# print(test1)
# print(test2)

"""
random damage rolls, and a change for double damage (crit)       =Done
different special moves for each class
teams of 3 against each other     =Done
1 team win when the other team has no health      =Done
random move choice, BUT with some things being a higher change fx, if an attack can kill it has higher change, and if you have low health the higher change for protecting, and if an ally has little health higher change to heal
move order by speed stat
cannot do anything when no health               =Done maybe??

make sure the special moves have text added so it is shown what special move is used
"""
