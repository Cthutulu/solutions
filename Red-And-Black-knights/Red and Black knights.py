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
"""

class Board:
    def __init__(self, size):
        self.size = size
        self.board = []
        self.offset_x = size // 2
        self.offset_y = size // 2

        for y in range(size):
            row = []

            for x in range(size):
                row.append(0)

            self.board.append(row)

        self.spiral = self.make_spiral()

        for s in range(len(self.spiral)):
            self.set_square_s(s, s)

    def make_spiral(self):
        spiral = [(0,0)]

        x = 0
        y = 0
        direction = 0
        distance = 1

        directions = [
            (1, 0),  # 0 Højre
            (0, 1),  # 1 Op
            (-1, 0),  # 2 Venstre
            (0, -1),  # 3 Ned
        ]

        # len(
        for z in range(20):
            dx, dy = directions[direction]

            for i in range(distance):
                x = x + dx
                y = y + dy

                spiral.append((x, y))

            direction = (direction + 1) % 4
            # direction = direction + 1

            # if direction == 4:
            #     direction = 0

            if z % 2 == 1:
                distance = distance + 1

        return spiral

    def set_square(self, x, y, value):
        self.board[y][x] = value

    def get_square(self, x, y):
        return self.board[y][x]

    def set_square_s(self, s, value):
        x, y = self.spiral[s]

        x = x + self.offset_x
        y = self.offset_y - y

        self.set_square(x, y, value)

board = Board(11)

for row in board.board:
    print(row)


# flyt helle dannelsen af spiral in i init
# get_square_s
# actually lav en spiral af tal
# gør så den nemt kans skifte mellem s tal (spiral tal), og x y tal

"""
(-3,3) (-2,3) (-1,3)  (0,3)  (1,3)  (2,3)  (3,3)
(-3,2) (-2,2) (-1,2)  (0,2)  (1,2)  (2,2)  (3,2)
(-3,1) (-2,1) (-1,1)  (0,1)  (1,1)  (2,1)  (3,1)
(-3,0) (-2,0) (-1,0)  (0,0)  (1,0)  (2,0)  (3,0)
(-3,-1)(-2,-1)(-1,-1) (0,-1) (1,-1) (2,-1) (3,-1)
(-3,-2)(-2,-2)(-1,-2) (0,-2) (1,-2) (2,-2) (3,-2)
(-3,-3)(-2,-3)(-1,-3) (0,-3) (1,-3) (2,-3) (3,-3)
"""

"""
en function med input x,y og output s
en klasse brik, med attributer, position, bevægelse dx og dy
function med input brik og output all truede fælter

"""