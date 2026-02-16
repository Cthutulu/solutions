"""
Kør dette program.
Tilføj oop-relaterede kommentarer til denne kode.
    Eksempler:
        class definition / klasse definition
        constructor / konstruktor
        inheritance / nedarvning
        object definition / objekt definition
        attribute / attribut
        method / metode
        polymorphism / polymorfisme
        encapsulation: protected attribute / indkapsling: beskyttet attribut
        encapsulation: protected method / indkapsling: beskyttet metode
"""


class Building:     #Class
    def __init__(self, area, floors, value):    #constructor
        self.area = area        #Attribute
        self.floors = floors    #Attribute
        self._value = value     #Protected attribute ( _ in front)

    def renovate(self):     #Method
        print("Installing an extra bathroom...")
        self._adjust_value(10)

    def _adjust_value(self, percentage):    #Protected method
        self._value *= 1 + (percentage / 100)
        print(f'Value has been adjusted by {percentage}% to {self._value:.2f}\n')


class Skyscraper(Building):

    def renovate(self):
        print("Installing a faster elevator.")
        self._adjust_value(6)


small_house = Building(160, 2, 200000)
skyscraper = Skyscraper(5000, 25, 10000000)

for building in [small_house, skyscraper]:
    print(f'This building has {building.floors} floors and an area of {building.area} square meters.')
    building.renovate()



