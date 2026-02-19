import random


class Animal:
    def __init__(self, name: str, sound: str, height: float, weight: float, legs: int, female: bool):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        return f"Animal: {self.name}, is {self.height} cm tall, and weigh {self.weight} kgs, it has {self.legs} legs"

    def make_noise(self):
        print(self.sound)


cow = Animal("Cow", "Mooooo",  134, 400, 4, True)

print(cow)
cow.make_noise()
print()


class Dog(Animal):
    def __init__(self, name: str, race: str, sound: str, height: float, weight: float, legs: int, tail_length: float, female: bool, hunts_sheep: bool):
        super().__init__(name, sound, height, weight, legs, female)
        self.race = race
        self.tail_length = tail_length
        self.hunt_sheep = hunts_sheep

    def __repr__(self):
        return f"Animal: {self.name}, this dog is a {self.race}, who is {self.height:.2f} cm tall, and weigh {self.weight:.2f} kgs, it has {self.legs} legs, does this dog hunt sheeps? {self.hunt_sheep}"

    def wag_tail(self):
        return f"This {self.race} wags with its {self.tail_length:.2f} cm long tail"

    def __add__(self, other):
        if isinstance(other, Dog):
            if self.female != other.female:
                mother = self if self.female else other
                father = other if not other.female else self

                baby_race = random.choice((mother.race, father.race))
                baby_gender = random.choice((True, False))
                baby_height = (random.uniform(mother.height / 4, father.height / 4))
                baby_weight = (random.uniform(mother.height / 4, father.height / 4))
                baby_tail_length = (random.uniform(mother.tail_length / 4, father.tail_length / 4))
                baby_hunts_sheep = random.choice((True, False))

                return Dog("puppy", baby_race, "woof", baby_height, baby_weight, 4, baby_tail_length, baby_gender, baby_hunts_sheep)

dog1 = Dog("Dog", "Collie", "Woof",  66, 27, 4, 6, True, False )
dog2 = Dog("Dog", "Collie", "Woof",  70, 30, 4, 7, False, False )

print(dog1)
dog1.make_noise()
print(dog1.wag_tail())
print()
print(dog2)
dog2.make_noise()
print(dog2.wag_tail())
print()

# def mate(mother, father):
#     if isinstance(mother, Dog) and isinstance(father, Dog):
#         if mother.female and not father.female:
#
#             baby_race = random.choice((mother.race, father.race))
#             baby_gender = random.choice((True, False))
#             baby_height = (random.uniform(mother.height / 4, father.height / 4))
#             baby_weight = (random.uniform(mother.height / 4, father.height / 4))
#             baby_tail_length = (random.uniform(mother.tail_length / 4, father.tail_length / 4))
#             baby_hunts_sheep = random.choice((True, False))
#
#             return Dog("puppy", baby_race, "woof", baby_height, baby_weight, 4, baby_tail_length, baby_gender, baby_hunts_sheep)


puppy = dog1 + dog2
print(puppy)
puppy.make_noise()
print(puppy.wag_tail())

