N = 8
RANGE = range(1, N + 1)  # 1, 2, 3, 4, 5, 6, 7, 8
DASH = ' -------------------'

# ***********
# DEBUG

# default, upper-left is (0, 0), bottom-right is (7, 7)
# chess_board = [[(i, j) for i in range(8)] for j in range(8)]

# Cartesian, bottom-left is (1, 1), upper-right is (8, 8)
# chess_board = list()
# for i in range(N):
#     line = list()
#     for j in range(N):
#         line.append((j + 1, N - i))
#     chess_board.append(line)

# board checker
# for line in chess_board:
#     print(line)

# GUBED
# ***********


def form_board(position: list[int] = None):
    # no position saving currently
    chess_board = list()
    for i in range(N):
        line = list()
        for j in range(N):
            line.append('X' if position and [j + 1, N - i] == position else '_')
        chess_board.append(line)

    return chess_board


def draw_board(board: [[str]]):
    for i, line in zip(range(8, 0, -1), board):
        print(f'{i}| {" ".join(line)} |')


def handle_input():
    while True:
        try:
            inp = [int(i) for i in input('Enter the knight\'s starting position: ').split()]
            if len(inp) == 2 and all(1 <= i <= 8 for i in inp):
                return inp
            raise ValueError
        except ValueError:
            print('Invalid dimensions!')


pos = handle_input()
print(DASH)
draw_board(form_board(pos))
print(DASH)
print(f'   {" ".join(str(i) for i in RANGE)} ')
