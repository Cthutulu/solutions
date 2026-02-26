"""Opgave "The inventory sequence"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=rBU9E-ZOZAI

Del 2:
    Skriv en funktion inventory(), som producerer de tal, der er vist i videoen.
    Funktionen accepterer en parameter, der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række.

    Du vil sandsynligvis ønske at definere en funktion count_number(), som tæller, hvor ofte
    et bestemt antal optræder i den aktuelle talrække.

Del 3:
    I hovedprogrammet kalder du inventory() med fx 6 som argument.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""


def inventory_variant(lines):
    sequence = [[0]]  # first line

    for _ in range(1, lines):
        current = []
        n = 0

        # count numbers sequentially until first 0
        while True:
            # count occurrences of n in all previous lines
            total_count = sum(line.count(n) for line in sequence)
            # also include numbers already in the current line
            total_count += current.count(n)

            current.append(total_count)

            if total_count == 0:  # stop at first 0
                break

            n += 1  # move to next number

        sequence.append(current)

    # print sequence
    for line in sequence:
        print(line)


# Test: first 10 lines
inventory_variant(15)