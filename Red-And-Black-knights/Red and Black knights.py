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
        # self.pieces = []

        self.players = [
            Player(1, "R", Knight),
            Player(2, "B", Knight)
        ]

        self.turn = 0

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

    def play(self):
        pass
        # player = self.players
        # piece =
        #
        #
        # self.turn = self.turn % len(self.players)

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

    def is_occupied_s(self, s):
        return isinstance(self.get_square_s(s), Piece)

    def is_available_s(self, s, player):
        if self.is_occupied_s(s):
            return False

        square = self.get_square_s(s)

        if square == 0:
            return True

        if square == player.value:
            return True

        return False

    def add_piece(self, piece, player):
        # self.pieces.append(piece)

        for s in range(len(self.spiral)):
            if self.is_available_s(s, player):
                x, y = self.s_to_xy(s)

                piece.x = x
                piece.y = y

                self.set_square_s(s, piece)

                self.mark_threatened_squares(piece)

                return s

    def mark_threatened_squares(self, piece):
        for s in piece.threatened_squares_s(self):
            if self.is_occupied_s(s):
                continue

            square = self.get_square_s(s)

            if square == 0:
                self.set_square_s(s, piece.value)

            elif square != piece.value:
                self.set_square_s(s, "-")


class Player:
    def __init__(self, value, color, piece_type):
        self.value = value
        self.color = color
        self.piece_type = piece_type


class Piece:
    def __init__(self, x, y, value, color):
        self.x = x
        self.y = y
        self.value = value
        self.color = color

    def __repr__(self):
        return self.color

    def threatened_squares(self):
        pass

    def threatened_squares_s(self, board):
        threatened = []

        for x, y in self.threatened_squares():
            s = board.xy_to_s(x, y)

            if s is not None:
                threatened.append(s)

        return threatened


class Knight(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

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


board = Board(7)

knight = Knight(None, None, 1, "R")
board.add_piece(knight, board.players[0])

knight2 = Knight(None, None, 2, "B")
board.add_piece(knight2, board.players[1])

knight = Knight(None, None, 1, "R")
board.add_piece(knight, board.players[0])

knight2 = Knight(None, None, 2, "B")
board.add_piece(knight2, board.players[1])

knight = Knight(None, None, 1, "R")
board.add_piece(knight, board.players[0])

knight2 = Knight(None, None, 2, "B")
board.add_piece(knight2, board.players[1])

knight = Knight(None, None, 1, "R")
board.add_piece(knight, board.players[0])

knight2 = Knight(None, None, 2, "B")
board.add_piece(knight2, board.players[1])

knight = Knight(None, None, 1, "R")
board.add_piece(knight, board.players[0])

knight2 = Knight(None, None, 2, "B")
board.add_piece(knight2, board.players[1])

knight = Knight(None, None, 1, "R")
board.add_piece(knight, board.players[0])
#
# print(knight.threatened_squares())
# print(knight.threatened_squares_s(board))

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