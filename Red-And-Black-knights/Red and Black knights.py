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

size = 11

board = []

for y in range(size):
    row = []

    for x in range(size):
        row.append(0)

    board.append(row)

offset_x = size // 2
offset_y = size // 2

directions = [
    (1, 0),     # 0 Højre
    (0, 1),     # 1 Op
    (-1, 0),    # 2 Venstre
    (0, -1),    # 3 Ned
]

direction = 0
distance = 1

board[0 + offset_x][0 + offset_y] = 1

# def set_square(row, col, value)
# def get_square()

for row in board:
    print(row)
# x = 0
# y = 0
#
# positions = [(0, 0)]
#
# directions = [
#     (1, 0),     # 0 Højre
#     (0, 1),     # 1 Op
#     (-1, 0),    # 2 Venstre
#     (0, -1),    # 3 Ned
# ]
#
# direction = 0
# distance = 1
#
# for z in range(6):
#     dx, dy = directions[direction]
#
#     for i in range(distance):
#         x = x + dx
#         y = y + dy
#
#         positions.append((x, y))
#
#     direction = (direction + 1) % 4
#     # direction = direction + 1
#
#     # if direction == 4:
#     #     direction = 0
#
#     if z % 2 == 1:
#         distance = distance + 1
#
#
# print(positions)


# board x * x
# a way to whem you append positions that it then gives a number there
#  @staticmethod
#     def some_funtion(test):
#         print(test)

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