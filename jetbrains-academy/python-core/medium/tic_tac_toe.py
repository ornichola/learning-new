DASH = ('-' * 9)
X, O, E = 'X', 'O', ' '
WEIGHTS = {X: 1, O: -1, E: 0}
MATRIX_DIMENSION = 3
MATRIX = [[E for _ in range(MATRIX_DIMENSION)] for _ in range(MATRIX_DIMENSION)]
TURN = X


def draw_matrix():
    print(DASH, '\n'.join(f"| {' '.join(cell for cell in line)} |" for line in MATRIX), DASH, sep='\n')


def _is_cell_occupied(coords):
    coords = [int(coord) - 1 for coord in coords]
    return MATRIX[coords[0]][coords[1]] != E


def _has_empty_cells():
    return any(any(cell == E for cell in line) for line in MATRIX)


def parse_coordinates(raw_input: str):
    coords = raw_input.split()
    if not all(c.isdigit() for c in coords):
        return 'error', 'You should enter numbers!'
    elif not all(1 <= int(c) <= 3 for c in coords):
        return 'error', 'Coordinates should be from 1 to 3!'
    elif _is_cell_occupied(coords):
        return 'error', 'This cell is occupied! Choose another one!'
    else:
        return list(int(c) for c in coords)


def __form_lines():
    """
    :return: game matrix transposed in lines for check winner
    """

    _lines = list()
    for i in range(MATRIX_DIMENSION):
        line_ij = list()  # rows
        line_ji = list()  # columns
        for j in range(MATRIX_DIMENSION):
            line_ij.append(MATRIX[i][j])
            line_ji.append(MATRIX[j][i])
        _lines.append(line_ij)
        _lines.append(line_ji)

    # diagonals
    _lines.append([MATRIX[0][0], MATRIX[1][1], MATRIX[2][2]])
    _lines.append([MATRIX[0][2], MATRIX[1][1], MATRIX[2][0]])

    return _lines


def place_cell(coords):
    global MATRIX, TURN
    coords = [int(coord) - 1 for coord in coords]
    MATRIX[coords[0]][coords[1]] = TURN
    TURN = O if TURN == X else X


def check_game_state():
    # replace X, O, _ with 1, -1, 0 for count sum of line -> if it's 3 - X wins, -3 - O wins
    weighted_lines = [[WEIGHTS[cell] for cell in line] for line in __form_lines()]

    state = {
        'is_game_finished': None,
        'winner': None,
    }
    for weighted_line in weighted_lines:
        if sum(weighted_line) == 3:
            state['is_game_finished'], state['winner'] = True, f'{X} wins'
        elif sum(weighted_line) == -3:
            state['is_game_finished'], state['winner'] = True, f'{O} wins'

    if not state['winner'] and not _has_empty_cells():
        state['is_game_finished'], state['winner'] = True, 'Draw'

    return state


draw_matrix()
while True:
    coordinates = parse_coordinates(input('Enter the coordinates: '))
    if 'error' in coordinates:
        print(coordinates[1])
        continue

    place_cell(coordinates)
    draw_matrix()
    game_state = check_game_state()
    if game_state.get('is_game_finished'):
        print(game_state['winner'])
        break
