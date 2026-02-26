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
    def __init__(self, name: str, health: int, p_attack: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int, starting_cooldown=0):
        self.name = name
        self.max_health = health
        self._current_health = health
        self.p_attack = p_attack
        self.m_attack = m_attack
        self.phy_defense = phy_defense
        self.mag_defense = mag_defense
        self.speed = speed
        self.special_cooldown = starting_cooldown
        self.special_used = False
        self.taunt_active = False
        self.berserk_active = False
        self.speed_buff_turns = 0
        self.untargetable_turns = 0
        self.stunned = False

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




class Paladin(Character):
    def __init__(self, name: str, health: int, p_attack: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int, starting_cooldown=2):
        super().__init__(name, health, p_attack, m_attack, phy_defense, mag_defense, speed, starting_cooldown)

    def __repr__(self):
        return f"{self.name} the Paladin has {self._current_health}/{self.max_health} health"

    def use_special(self, target, _):
        return self.radiant_strike(target)

    def radiant_strike(self, other):
        if self.is_alive() and self.special_cooldown == 0:
            damage = self.m_attack
            crit = random.random() < 0.10
            if crit: damage *= 2.2
            variation = random.uniform(1.45, 1.55)
            damage = round(damage * variation)
            print(f"{self.name} uses Radiant Strike on {other.name} for {damage} damage", end="")
            if crit:
                print(" (CRITICAL HIT!)")
            else:
                print()
            other._take_m_damage(damage)
            self.special_cooldown = 3
            return True
        return False


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
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int, starting_cooldown=2):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed, starting_cooldown)
        self.untargetable = False
        self.untargetable_turns = 0

    def __repr__(self):
        return f"{self.name} the Rouge has {self._current_health}/{self.max_health} health"

    def use_special(self, target, _):
        return self.backstab(target)

    def backstab(self, other):
        if self.is_alive() and not self.special_used and self.special_cooldown == 0:
            damage = round(self.p_attack * 2.0)
            print(f"{self.name} uses Backstab on {other.name} for {damage} damage!")
            other._take_p_damage(damage)
            self.special_used = True
            self.special_cooldown = 2
            return True
        return False

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
    def __init__(self, name: str, health: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int, starting_cooldown=2):
        super().__init__(name, health, 0, m_attack, phy_defense, mag_defense, speed, starting_cooldown)

    def __repr__(self):
        return f"{self.name} the Mage has {self._current_health}/{self.max_health} health"

    def use_special(self, target, _):
        return self.mana_burst(target)

    def mana_burst(self, other):
        if self.is_alive() and not self.special_used and self.special_cooldown == 0:
            damage = round(self.m_attack * 2.0)
            print(f"{self.name} casts Mana Burst on {other.name} for {damage} damage!")
            other._take_m_damage(damage)
            self.special_used = True
            self.special_cooldown = 2
            return True
        return False

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

    def use_special(self, target=None, allies=None):
        return self.check_berserk()

    def check_berserk(self):
        if not self.berserk_active and self.is_alive() and self._current_health < self.max_health * 0.4:
            self.berserk_active = True
            self.p_attack = int(self.p_attack * 1.5)
            self.phy_defense = 5
            self.mag_defense = 5
            print(f"{self.name} goes Berserk! Damage is increased at the cost of defense until death!")

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
    def __init__(self, name: str, health: int, p_attack: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int, starting_cooldown=1):
        super().__init__(name, health, p_attack, m_attack, phy_defense, mag_defense, speed, starting_cooldown)

    def __repr__(self):
        return f"{self.name} the Ranger has {self._current_health}/{self.max_health} health"

    def use_special(self, target, _):
        return self.spirit_arrow(target)

    def spirit_arrow(self, other):
        if self.is_alive() and self.special_cooldown == 0:
            damage = self.m_attack
            crit = random.random() < 0.3
            if crit: damage *= 2.3
            variation = random.uniform(1.35, 1.55)
            damage = round(damage * variation)
            print(f"{self.name} uses Spirit Arrow on {other.name} for {damage} damage", end="")
            if crit: print(" (CRITICAL HIT!)")
            else: print()
            other._take_m_damage(damage)
            self.special_cooldown = 2
            return True
        return False

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
    def __init__(self, name: str, health: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int, starting_cooldown=1):
        super().__init__(name, health, 0, m_attack, phy_defense, mag_defense, speed, starting_cooldown)

    def __repr__(self):
        return f"{self.name} the Bard has {self._current_health}/{self.max_health} health"

    def use_special(self, _, allies):
        return self.hymn_of_haste(allies)

    def hymn_of_haste(self, allies):
        if self.is_alive() and self.special_cooldown == 0:
            for ally in allies:
                if ally.is_alive():
                    ally.speed = int(ally.speed * 1.5)
                    ally.speed_buff_turns = 2
            self.special_cooldown = 4
            print(f"{self.name} casts Hymn of Haste! Allies speed is increased for 2 turns!")
            return True
        return False

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
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int, starting_cooldown=2):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed, starting_cooldown)

    def __repr__(self):
        return f"{self.name} the Warrior has {self._current_health}/{self.max_health} health"

    def use_special(self, target, _):
        return self.shield_bash(target)

    def shield_bash(self, target):
        if self.is_alive() and self.special_cooldown == 0:
            damage = round(self.p_attack * 0.5)
            print(f"{self.name} uses Shield Bash on {target.name} for {damage} damage! {target.name} is stunned next turn!")
            target._take_p_damage(damage)
            target.stunned = True
            self.special_cooldown = 3
            return True
        return False

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
    def __init__(self, name: str, health: int, p_attack: int, phy_defense: int, mag_defense: int, speed: int, starting_cooldown=1):
        super().__init__(name, health, p_attack, 0, phy_defense, mag_defense, speed, starting_cooldown)

    def __repr__(self):
        return f"{self.name} the Tank has {self._current_health}/{self.max_health} health"

    def use_special(self, target=None, allies=None):
        return self.taunt()

    def taunt(self):
        if self.is_alive() and self.special_cooldown == 0:
            self.taunt_active = True
            self.taunt_turns = 2
            self.special_cooldown = 4
            print(f"{self.name} uses Taunt! Enemies must attack him for 2 turns!")
            return True
        return False

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
    def __init__(self, name: str, health: int, m_attack: int, phy_defense: int, mag_defense: int, speed: int, starting_cooldown=1):
        super().__init__(name, health, 0, m_attack, phy_defense, mag_defense, speed, starting_cooldown)
        self.untargetable = False
        self.untargetable_turns = 0

    def __repr__(self):
        return f"{self.name} the Priest has {self._current_health}/{self.max_health} health"

    def use_special(self, _, allies):
        return self.holy_bastion(allies)

    def normal_attack(self, allies):
        if self.is_alive():
            injured_allies = [a for a in allies if a.is_alive() and a._current_health < a.max_health]
            if injured_allies:
                target = min(injured_allies, key=lambda x: x._current_health)  # hopefully will heal ally with least hp maybe
                heal_amount = int(self.m_attack / 1.5)
                target._get_healed(heal_amount)
                print(f"{self.name} heals {target.name} for {heal_amount} HP")

    def holy_bastion(self, allies):
        if self.is_alive() and not self.special_used:
            if any(a.is_alive() and a._current_health <= a.max_health * 0.7 for a in allies):
                self.special_used = True
                self.untargetable = True
                self.untargetable_turns = 3
                print(f"{self.name} casts Holy Bastion! Priest cannot be targeted for 3 turns!")
                for ally in allies:
                    if ally.is_alive() and ally._current_health < ally.max_health:
                        heal_amount = int(self.m_attack / 2.5)
                        ally._get_healed(heal_amount)
                        print(f"{self.name} heals {ally.name} for {heal_amount} HP")
                return True
        return False


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


        turn_order = team1 + team2

        turn_order.sort(key=lambda c: c.speed, reverse=True)

        for char in turn_order:

            if not char.is_alive():
                continue

            if char.special_cooldown > 0:
                char.special_cooldown -= 1

                # for special attacks that is activated over multiple turns
            if getattr(char, "taunt_active", False):
                char.taunt_turns -= 1
                if char.taunt_turns <= 0:
                    char.taunt_active = False
                    print(f"{char.name}'s Taunt has ended!")

            if getattr(char, "speed_buff_turns", 0) > 0:
                char.speed_buff_turns -= 1
                if char.speed_buff_turns <= 0:
                    print(f"{char.name}'s speed buff has ended!")

            if getattr(char, "untargetable_turns", 0) > 0:
                char.untargetable_turns -= 1
                if char.untargetable_turns <= 0:
                    char.untargetable = False
                    print(f"{char.name} is now targetable again.")

                # to skip turn if character is stunned
            if getattr(char, "stunned", False):
                print(f"{char.name} is stunned and cannot act!")
                char.stunned = False  # Stun lasts only 1 turn
                continue

            if isinstance(char, Barbarian):
                char.check_berserk()

            if char in team1:
                allies = team1
                enemies = team2
            else:
                allies = team2
                enemies = team1

            def select_target(enemy_list):
                alive = [e for e in enemy_list if e.is_alive() and not getattr(e, "untargetable", False)]
                if not alive:  # fallback
                    alive = [e for e in enemy_list if e.is_alive()]

                taunt_targets = [e for e in alive if getattr(e, "taunt_active", False)]
                if taunt_targets:
                    return random.choice(taunt_targets)
                return random.choice(alive) if alive else None

            target = select_target(enemies)

            used_special = char.use_special(target, allies)

            if not used_special:
                if isinstance(char, Priest):
                    char.normal_attack(allies)
                elif target:
                    char.normal_attack(target)

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
different special moves for each class    =Done
teams of 3 against each other     =Done
1 team win when the other team has no health      =Done
random move choice, BUT with some things being a higher change fx, if an attack can kill it has higher change, and if you have low health the higher change for protecting, and if an ally has little health higher change to heal     =kinda Done
move order by speed stat            =Done
cannot do anything when no health               =Done
make sure the special moves have text added so it is shown what special move is used      =Done
"""
