import random


DOMINOES = list()
PIECES_COMPUTER = list()
PIECES_PLAYER = list()
LINE = list()
TURN = None
WINNER = None


def form_dominoes() -> [[int]]:
    n = 7
    return [[i, j] for i in range(n) for j in range(i, n)]


def handle_pieces():
    max_per_player = 7
    global DOMINOES, PIECES_COMPUTER, PIECES_PLAYER
    DOMINOES = form_dominoes()
    PIECES_COMPUTER = [DOMINOES.pop(DOMINOES.index(random.choice(DOMINOES))) for _ in range(max_per_player)]
    PIECES_PLAYER = [DOMINOES.pop(DOMINOES.index(random.choice(DOMINOES))) for _ in range(max_per_player)]


def setup_table():
    global DOMINOES, PIECES_COMPUTER, PIECES_PLAYER, LINE, TURN
    starting_domino, biggest_value = None, 0
    while not starting_domino:
        handle_pieces()
        chose_from = PIECES_COMPUTER + PIECES_PLAYER
        for domino in chose_from:
            if domino[0] == domino[1] and sum(domino) > biggest_value:
                starting_domino, biggest_value = domino, sum(domino)
        if not starting_domino:
            continue
        else:
            if starting_domino in PIECES_COMPUTER:
                PIECES_COMPUTER.remove(starting_domino)
                TURN = 'player'
            else:
                PIECES_PLAYER.remove(starting_domino)
                TURN = 'computer'

            LINE.append(starting_domino)


def draw_interface():
    print('======================================================================')
    print(f'Stock size: {len(DOMINOES)}')
    print(f'Computer pieces: {len(PIECES_COMPUTER)}')
    if len(LINE) < 7:
        print(f'\n{"".join(str(d) for d in LINE)}\n')
    else:
        print(f'{"".join(str(d) for d in LINE[0:3])}...{"".join(str(d) for d in LINE[-3:-1])}')
    print('Your pieces:')
    for n, p in enumerate(PIECES_PLAYER, start=1):
        print(f'{n}:{p}')
    if TURN == 'computer':
        print('\nStatus: Computer is about to make a move. Press Enter to continue...')
    else:
        print('\nStatus: It\'s your turn to make a move. Enter your command.')


def _handle_user_input():
    while True:
        try:
            domino_index = int(input())
            if abs(domino_index) not in range(0, len(PIECES_PLAYER) + 1):
                raise ValueError
            break
        except ValueError:
            print('Invalid input. Please try again.')
            continue
    return domino_index


def start_game_loop():
    global TURN, WINNER
    while True:
        if TURN == 'player':
            player_domino_index = _handle_user_input()
            if player_domino_index == 0:
                if DOMINOES:
                    PIECES_PLAYER.append(DOMINOES.pop(DOMINOES.index(random.choice(DOMINOES))))
                    TURN = 'computer'
                else:
                    continue
            else:
                if PIECES_PLAYER:
                    inserting_domino = PIECES_PLAYER.pop(abs(player_domino_index) - 1)

                    # processing move availability
                    border_domino = LINE[-1] if player_domino_index > 0 else LINE[0]
                    border = border_domino[-1] if player_domino_index > 0 else border_domino[0]
                    if any(b == border for b in inserting_domino):
                        if player_domino_index < 0 and inserting_domino[0] == border:
                            inserting_domino.reverse()
                        if player_domino_index > 0 and inserting_domino[1] == border:
                            inserting_domino.reverse()
                    else:
                        print('Illegal move. Please try again.')
                        continue

                    if player_domino_index > 0:
                        LINE.append(inserting_domino)
                    else:
                        LINE.insert(0, inserting_domino)
                    TURN = 'computer'
                else:
                    WINNER = TURN
                    break
        else:
            computer_size = len(PIECES_COMPUTER)
            if computer_size:
                input()
                TURN = 'player'

                # handling computer move
                borders = {'left': LINE[0][0], 'right': LINE[-1][-1]}
                for domino in PIECES_COMPUTER:
                    if domino[0] == borders['left']:
                        domino.reverse()
                        LINE.insert(0, domino)
                        break
                    elif domino[1] == borders['left']:
                        LINE.insert(0, domino)
                        break
                    elif domino[0] == borders['right']:
                        LINE.append(domino)
                        break
                    elif domino[1] == borders['right']:
                        domino.reverse()
                        LINE.append(domino)
                        break
                else:
                    if DOMINOES:
                        PIECES_COMPUTER.append(DOMINOES.pop(DOMINOES.index(random.choice(DOMINOES))))
            else:
                WINNER = TURN
                break

        # check draw condition
        snake = [n for d in LINE for n in d]
        if snake[0] == snake[-1]:
            if snake.count(snake[0]) == 8:
                WINNER = 'draw'
                break

        draw_interface()


setup_table()
draw_interface()
start_game_loop()

# print out winner
if WINNER == 'player':
    print('Status: The game is over. You won!')
elif WINNER == 'computer':
    print('Status: The game is over. The computer won!')
elif WINNER == 'draw':
    print('Status: The game is over. It\'s a draw!')
else:
    print('Something went completely wrong')
