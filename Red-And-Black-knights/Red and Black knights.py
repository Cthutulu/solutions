"""
- Bræt
    * spiral fra 0 til x
    * med x = højeste tal og derfor størrelsen på brættet

- Brikker
    * forskellige klasser
        * kan flytte sig på forskellige måder
        * forskellige farver
    * en måde at sige hvilke brikker der skal bruges
    * en måde at sige hvor mange  forskellige farver der skal være

- placering og regler
    * første brik skal placeres på 0
    * brikker skal placeres på det mindste felt, der ikke er optaget eller kan "angribes"
    * skifte mellem alle aktive brikker
    * brikker kan "angribe" tomme felter

- resultat
    * danne et resultat man kan se
    * skal kunne passe til skærmen lige meget størrelsen
    * zoome ind og ud



xy cords
(2k+1)^2−1
"""


x = 0
y = 0

directions = [
    (1, 0),     # 0 Højre
    (0, 1),     # 1 Op
    (-1, 0),    # 2 Venstre
    (0, -1),    # 3 Ned
]

direction = 2
distance = 2


dx, dy = directions[direction]

for i in range(distance):
    x = x + dx
    y = y + dy

print(x, y)


"""
(-3,3) (-2,3) (-1,3)  (0,3)  (1,3)  (2,3)  (3,3)
(-3,2) (-2,2) (-1,2)  (0,2)  (1,2)  (2,2)  (3,2)
(-3,1) (-2,1) (-1,1)  (0,1)  (1,1)  (2,1)  (3,1)
(-3,0) (-2,0) (-1,0)  (0,0)  (1,0)  (2,0)  (3,0)
(-3,-1)(-2,-1)(-1,-1) (0,-1) (1,-1) (2,-1) (3,-1)
(-3,-2)(-2,-2)(-1,-2) (0,-2) (1,-2) (2,-2) (3,-2)
(-3,-3)(-2,-3)(-1,-3) (0,-3) (1,-3) (2,-3) (3,-3)
"""