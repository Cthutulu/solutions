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
            self.append(c)
            print(self)

    def plus(self, other):
        result = LunarInt("")
        print(result)



        # dummy = "abcdefg"
        # for i in range(4):
        #     print(dummy[-i])
        #
        # if number_1 > number_2:
        #     for x in self.number_1:
        #         if self.number_1[-1] > self.number_2[-1]:
        #             print("test1")
        #         else:
        #             print("test2")
        # else:
        #     for x in self.number_2:
        #         if self.number_1[-1] > self.number_2[-1]:
        #             print("test3")
        #         else:
        #             print("test 4")

# "range(11, 6, -1)"

    def multiply(self):
        pass
number_1 = "567"
number_2 = "7390"
lunar1 = LunarInt(number_1)
lunar2 = LunarInt(number_2)
lunar3 = lunar1.plus(lunar2)

# if number_1 > number_2:
#     for x in str(number_1):
#         print(x)
#
# else:
#     for x in str(number_2):
#         if number_2 > number_1:
#             print(x)
#         else:
#             print(x)






