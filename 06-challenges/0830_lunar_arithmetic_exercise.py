"""Opgave "Lunar arithmetic"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=cZkGeR9CWbk

Del 2:
    Skriv en klasse Lunar_int(), med metoder, der gør, at du kan anvende operatorerne + og * på
    objekter af denne klasse, og at resultaterne svarer til de regler, der forklares i videoen.

Del 3:
    Se resten af videoen.

Del 4:
    Skriv en funktion calc_lunar_primes(n), som retunerer en liste med de første n lunar primes.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
class LunarInt(list):
    def __init__(self, number_str):
        super().__init__()
        for c in number_str:
            self.append(int(c))


    def __repr__(self):
        result = ""
        for y in self:
            result += str(y)
        return result


    def plus(self, other):
        if len(self) > len(other):
            longer = self
            shorter = other
        else:
            shorter = self
            longer = other

        test = []
        test2 = []

        for x in range(1, len(longer) + 1):
            if x <= len(shorter):
                test.append([longer[-x], shorter[-x]])
            else:
                test.append([longer[-x]])

            # print(test)

            test2.append(max(test[-1]))
            # print(test2)

        result = LunarInt([*reversed(test2)])
        return result


    def multiply(self, other):
        if len(self) > len(other):
            longer = self
            shorter = other
        else:
            shorter = self
            longer = other

        for y in range(1, len(shorter) + 1):
            current_digit = shorter[-y]

            test = []

            for x in range(1, len(longer) + 1):
                test.append([longer[-x], current_digit])

            print(test)

        # test = []
        # test2 = []
        #
        # for x in range(1, len(longer) + 1):
        #     if x <= len(shorter):
        #         test.append([longer[-x], shorter[-x]])
        #     else:
        #         test.append([longer[-x]])
        #
        #     print(test)
        #
        #     test2.append(min(test[-1]))
        #     print(test2)

        # result = LunarInt([*reversed(test2)])
        # return result


number_1 = "2468"
number_2 = "753"
lunar1 = LunarInt(number_1)
lunar2 = LunarInt(number_2)
lunar3 = lunar1.plus(lunar2)
print(lunar1.plus(lunar2))
lunar4 = lunar1.multiply(lunar2)







