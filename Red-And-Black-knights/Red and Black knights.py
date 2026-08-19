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

    def set_square(self, x, y, value):
        self.board[y][x] = value

    def get_square(self, x, y):
        return self.board[y][x]

    def set_square_s(self, s, value):
        x, y = self.spiral[s]

        x = x + self.offset_x
        y = y + self.offset_y

        self.set_square(x, y, value)

board = Board(11)

board.set_square(board.offset_x, board.offset_y, 1)

x = 0
y = 0
number = 0

board.set_square(x + board.offset_x, y + board.offset_y, number)

spiral = [(0, 0)]

directions = [
    (1, 0),     # 0 Højre
    (0, 1),     # 1 Op
    (-1, 0),    # 2 Venstre
    (0, -1),    # 3 Ned
]

direction = 0
distance = 1

for z in range(6):
    dx, dy = directions[direction]

    for i in range(distance):
        x = x + dx
        y = y + dy

        number = number + 1

        spiral.append((x, y))

    direction = (direction + 1) % 4
    # direction = direction + 1

    # if direction == 4:
    #     direction = 0

    if z % 2 == 1:
        distance = distance + 1

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

# class knight/brik: