# reading board dimension in COLUMNS ROWS format
while True:
    try:
        dimensions = [int(i) for i in input('Enter your board dimensions: ').split()]
        if len(dimensions) != 2 or any(d <= 0 for d in dimensions):
            raise ValueError
        break
    except ValueError:
        print('Invalid dimensions!')

# forming some intermediate data
cell_size = len(str(dimensions[0] * dimensions[1]))
border = f'{" " * len(str(dimensions[0]))}{"-" * (dimensions[0] * (cell_size + 1) + 3)}'
board = [['_' * cell_size for _ in range(dimensions[0])] for _ in range(dimensions[1])]

# reading knight position
# remember that (1, 1) is a bottom left and (max_column, max_row) is an upper right
while True:
    try:
        position = [int(p) for p in input('Enter the knight\'s starting position: ').split()]
        if len(position) == 2 and all([1 <= position[0] <= dimensions[0], 1 <= position[1] <= dimensions[1]]):
            break
        raise ValueError
    except ValueError:
        print('Invalid position!')

# placing knight
for i in range(dimensions[1]):      # rows      0 1 2 3 4 (5)       for 6 5 input in dimension
    for j in range(dimensions[0]):  # columns   0 1 2 3 4 5 (6)     for 6 5 input in dimension
        # represent python form of list indexes as human-readable and as expected in tests
        column_id = j + 1
        row_id = dimensions[1] - i
        if [column_id, row_id] == position:
            # as far as cells represented as '_' * cell_size and strings are immutable
            cell = list(board[i][j])
            cell = [' ' for _ in cell]
            cell[-1] = 'X'
            board[i][j] = ''.join(cell)


# placing first possible moves
for i in range(dimensions[1]):
    for j in range(dimensions[0]):
        column_id = j + 1
        row_id = dimensions[1] - i
        # L-shape move is possible if diff between axes and initial position is 2, 1 or 1, 2
        vertical_possibility = abs(position[0] - column_id) == 2 and abs(position[1] - row_id) == 1
        horizontal_possibility = abs(position[0] - column_id) == 1 and abs(position[1] - row_id) == 2
        if vertical_possibility or horizontal_possibility:
            cell = list(board[i][j])
            cell = [' ' for _ in cell]
            cell[-1] = 'O'
            board[i][j] = ''.join(cell)


# printing whole field with placed knight
print(border)
for i, line in zip(range(len(board), 0, -1), board):
    index = f'{" " * (len(str(len(board))) - len(str(i)))}{i}'  # how many spaces should be before each row number
    print(f'{index}| {" ".join(line)} |')
print(border)

# printing footer nums
spaces_before_nums_range = ' ' * (len(str(len(board))) + 2)
nums_range = ' '.join([f'{" " * (cell_size - len(str(n)))}{str(n)}' for n in range(1, dimensions[0] + 1)])
print(f'{spaces_before_nums_range}{nums_range}')
