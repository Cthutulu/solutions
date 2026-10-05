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

import time
import cProfile
import pstats
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Board:
    def __init__(self, size):
        self.size = size
        self.board = []
        self.offset_x = size // 2
        self.offset_y = size // 2
        # self.pieces = []

        self.players = [
            Player(1, "R", Vazir),
            Player(2, "B", Vazir),
            Player(3, "Y", Vazir),
        ]

        self.turn = 0

        self.find_time = 0
        self.threat_time = 0

        # Rule change: all players have to threaten a square to make it inaccessible
        self.threatened_by = {}

        for y in range(size):
            row = []

            for x in range(size):
                row.append(0)

            self.board.append(row)

        self.spiral = self.make_spiral()

        self.xy_to_spiral = {}

        for s, (x, y) in enumerate(self.spiral):
            self.xy_to_spiral[(x, y)] = s

        for player in self.players:
            player.available = set(range(len(self.spiral)))

    def make_spiral(self):
        spiral = [(0, 0)]

        x = 0
        y = 0
        direction = 0
        distance = 1

        directions = [
            (1, 0),   # Højre
            (0, 1),   # Op
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
        continue_coloring = 0

        while continue_coloring < len(self.players):
            player = self.players[self.turn]
            piece = player.piece_type(
                None,
                None,
                player.value,
                player.color
            )

            if self.add_piece(piece, player) is None:
                continue_coloring += 1
            else:
                continue_coloring = 0

            self.turn = (self.turn + 1) % len(self.players)

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
        start = time.perf_counter()

        available = player.available

        if not available:
            return None

        s = available.pop()
        #
        for other_player in self.players:
            if other_player is not player:
                other_player.available.discard(s)

        x, y = self.s_to_xy(s)

        piece.x = x
        piece.y = y

        self.set_square_s(s, piece)

        self.find_time += time.perf_counter() - start

        start = time.perf_counter()

        self.mark_threatened_squares(piece, player)

        self.threat_time += time.perf_counter() - start

        return s

    def mark_threatened_squares(self, piece, player):
        for s in piece.threatened_squares_s(self):
            if self.is_occupied_s(s):
                continue

            # Original Rule

            square = self.get_square_s(s)


            if square == 0:
                self.set_square_s(s, piece.value)

                for other_player in self.players:
                    if other_player is not player:
                        other_player.available.discard(s)

            elif square != piece.value:
                self.set_square_s(s, "-")

                for other_player in self.players:
                    other_player.available.discard(s)


            # Rule change: all players have to threaten a square to make it inaccessible

            # if s not in self.threatened_by:
            #     self.threatened_by[s] = set()
            #
            # self.threatened_by[s].add(player.value)
            #
            # if len(self.threatened_by[s]) == len(self.players):
            #     self.set_square_s(s, "-")
            #
            #     for other_player in self.players:
            #         other_player.available.discard(s)


    def show(self):
        color_indices = {
            "R": 1,
            "B": 2,
            "Y": 3,
            "-": 4,

        }
        player_colors = {player.value: player.color for player in self.players}

        image = []
        for row in self.board:
            image_row = []
            for square in row:
                if isinstance(square, Piece):
                    color = square.color
                elif square == "-":
                    color = "-"
                else:
                    color = player_colors.get(square)

                image_row.append(color_indices.get(color, 0))
            image.append(image_row)

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(
            image,
            cmap=ListedColormap([
                "white",
                "red",
                "Blue",
                "yellow",
                "grey",
            ]),
            vmin=0,
            vmax=4,
            interpolation="nearest",
        )
        ax.set_axis_off()
        ax.set_title("Red and Black Knights")
        fig.tight_layout()
        plt.show()


class Player:
    def __init__(self, value, color, piece_type):
        self.value = value
        self.color = color
        self.piece_type = piece_type
        self.available = set()
        # self.available = list()


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



# region class Knight
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
# endregion

# region class Fers
class Fers(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

    MOVES = [
        (1, -1),
        (1, 1),
        (-1, 1),
        (-1, -1)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened
# endregion

# region class Vazir
class Vazir(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

    MOVES = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened
# endregion

# region class Camel
class Camel(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

    MOVES = [
        (3, -1),
        (3, 1),
        (1, 3),
        (-1, 3),
        (-3, 1),
        (-3, -1),
        (-1, -3),
        (1, -3)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened
# endregion

# region class Zebra
class Zebra(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

    MOVES = [
        (2, -3),
        (2, 3),
        (3, 2),
        (-3, 2),
        (-2, 3),
        (-2, -3),
        (-3, -2),
        (3, -2)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened
# endregion

# region class Antelope
class Antelope(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

    MOVES = [
        (4, -3),
        (4, 3),
        (3, 4),
        (-3, 4),
        (-4, 3),
        (-4, -3),
        (-3, -4),
        (3, -4)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened
# endregion

# region class Eland
class Eland(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

    MOVES = [
        (5, -3),
        (5, 3),
        (3, 5),
        (-3, 5),
        (-5, 3),
        (-5, -3),
        (-3, -5),
        (3, -5)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened
# endregion

# region class Satrap
class Satrap(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

    MOVES = [
        (2, 0),
        (-2, 0),
        (0, 2),
        (0, -2)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened
# endregion

# region class Aspbad
class Aspbad(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

    MOVES = [
        (2, -2),
        (2, 2),
        (-2, 2),
        (-2, -2)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened
# endregion

# region class Spehbed
class Spehbed(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

    MOVES = [
        (3, 0),
        (-3, 0),
        (0, 3),
        (0, -3)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened
# endregion

# region class Marzban
class Marzban(Piece):

    def __init__(self, x, y, value, color):
        super().__init__(x, y, value, color)

    MOVES = [
        (3, -3),
        (3, 3),
        (-3, 3),
        (-3, -3)
    ]

    def threatened_squares(self):
        threatened = []

        for dx, dy in self.MOVES:
            x = self.x + dx
            y = self.y + dy

            threatened.append((x, y))

        return threatened
# endregion

def main():
    board = Board(1001)
    board.play()

    print("Find time:", board.find_time)
    print("Threat time:", board.threat_time)

    # for row in board.board:
    #     print(row)
    board.show()

# with cProfile.Profile() as pr:
#     main()
# stats = pstats.Stats(pr)
# stats.sort_stats(pstats.SortKey.CUMULATIVE)
# stats.print_stats()

main()


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
Cool patterns:
Normal rule:
3 Vazir


Rule change:
1 Vazir + 1 Fers



"""