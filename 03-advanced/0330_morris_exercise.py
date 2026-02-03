"""
Opgave "Morris the Miner":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn 0332_morris_help.py og start derfra.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""

morris = { "turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whiskey": 0, "gold": 0,}


def nominus():
    for stats in ("sleepiness", "thirst", "hunger"):
        morris[stats] = max(0, morris[stats])


def death():
    return any(morris[stats] >= 100 for stats in ("sleepiness", "thirst", "hunger"))



def sleep():
    morris["sleepiness"] -= 10
    morris["thirst"] += 5
    morris["hunger"] += 5

def mine():
    morris["sleepiness"] += 5
    morris["thirst"] += 10
    morris["hunger"] += 10
    morris["gold"] += 10

def eat():
    if morris["gold"] >= 2:
        morris["sleepiness"] += 5
        morris["thirst"] -= 5
        morris["hunger"] -= 15
        morris["gold"] -= 2

def buy_whiskey():
    if morris["gold"] >= 1:
        morris["sleepiness"] += 5
        morris["thirst"] += 1
        morris["hunger"] += 1
        morris["whiskey"] += 1
        morris["gold"] -= 1

def drink():
    if morris["whiskey"] >= 1:
        morris["sleepiness"] += 5
        morris["thirst"] -= 17
        morris["hunger"] += 1
        morris["whiskey"] -= 1

def rest():
    morris["sleepiness"] -= 5
    morris["thirst"] += 3
    morris["hunger"] += 3

def rent():
    morris["gold"] -= 25




while morris["turn"] < 1000:

    morris["turn"] += 1

    # Work Days:
    if morris["turn"] % 7 in (1, 2, 3, 4, 5):
        if morris["sleepiness"] >= 60:
            eat()
            rest()
            sleep()
        elif morris["gold"] < 10:
           mine()
           mine()
           eat()
           sleep()
        else:
            mine()
            eat()
            sleep()

    # Wekend:
    if morris["turn"] % 7 in (0, 6):
        eat()
        buy_whiskey()
        drink()
        sleep()

    # Rent Day: :(
    if morris["turn"] % 7 in (0,):
        rent()

    # For those hungry and thirsty moments:
    if morris["thirst"] > 60:
        while morris["thirst"] > 50:
            buy_whiskey()
            drink()

    if morris["hunger"] > 60:
        while morris["hunger"] > 40:
            eat()


    if death():
        print("Game Over")
        break

    nominus()


    print(morris)

