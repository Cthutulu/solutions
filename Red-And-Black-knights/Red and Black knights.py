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

        self.xy_to_spiral = {}

        for s, (x, y) in enumerate(self.spiral):
            self.xy_to_spiral[(x, y)] = s

            # self.set_square_s(s, s)

    def make_spiral(self):
        spiral = [(0, 0)]

        x = 0
        y = 0
        direction = 0
        distance = 1

        directions = [
            (1, 0),  # Højre
            (0, 1),  # Op
            (-1, 0),  # Venstre
            (0, -1),  # Ned
        ]

        while len(spiral) < self.size * self.size:
            dx, dy = directions[direction]

            for i in range(distance):
                x = x + dx
                y = y + dy

                if len(spiral) < self.size * self.size:
                    spiral.append((x, y))

            direction = (direction + 1) % 4

            if direction % 2 == 0:
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

    def get_square_s(self, s):
        x, y = self.spiral[s]

        x = x + self.offset_x
        y = self.offset_y - y

        return self.get_square(x, y)

    def s_to_xy(self, s):
        return self.spiral[s]

    def xy_to_s(self, x, y):
        return self.xy_to_spiral.get((x, y))

    def mark_threatened_squares(self, piece):
        for s in piece.threatened_squares_s(self):
            self.set_square_s(s, 1)




class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def threatened_squares(self):
        pass

    def threatened_squares_s(self, board):
        pass



class Knight(Piece):

    def __init__(self, x, y):
        super().__init__(x, y)

    MOVES = [
        (2, -1),
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened

    def threatened_squares_s(self, board):
        threatened = []

        for x, y in self.threatened_squares():
            s = board.xy_to_s(x, y)

            if s is not None: threatened.append(s)

        return threatened


board = Board(11)

knight = Knight(0, 0)

board.mark_threatened_squares(knight)

print(knight.threatened_squares())
print(knight.threatened_squares_s(board))

for row in board.board:
    print(row)

"""
(-3,3) (-2,3) (-1,3)  (0,3)  (1,3)  (2,3)  (3,3)
(-3,2) (-2,2) (-1,2)  (0,2)  (1,2)  (2,2)  (3,2)
(-3,1) (-2,1) (-1,1)  (0,1)  (1,1)  (2,1)  (3,1)
(-3,0) (-2,0) (-1,0)  (0,0)  (1,0)  (2,0)  (3,0)
(-3,-1)(-2,-1)(-1,-1) (0,-1) (1,-1) (2,-1) (3,-1)
(-3,-2)(-2,-2)(-1,-2) (0,-2) (1,-2) (2,-2) (3,-2)
(-3,-3)(-2,-3)(-1,-3) (0,-3) (1,-3) (2,-3) (3,-3)
"""

# matplotlib