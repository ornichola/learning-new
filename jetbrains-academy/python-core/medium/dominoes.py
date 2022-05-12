import random


class DominoesGame:
    def __init__(self):
        self.dominoes = list()
        self.pieces_computer = list()
        self.pieces_player = list()
        self.line = list()
        self.turn = None
        self.winner = None

    def form_dominoes(self):
        self.dominoes = [[i, j] for i in range(7) for j in range(i, 7)]

    def handle_players(self):
        self.pieces_computer = [self.dominoes.pop(self.dominoes.index(random.choice(self.dominoes))) for _ in range(7)]
        self.pieces_player = [self.dominoes.pop(self.dominoes.index(random.choice(self.dominoes))) for _ in range(7)]

    def switch_turn(self):
        self.turn = 'computer' if self.turn == 'player' else 'player'

    def setup_table(self):
        # handling dominoes on players hand until biggest equal can be placed
        starting_domino, biggest_value = None, 0
        while not starting_domino:
            self.form_dominoes()
            self.handle_players()
            chose_from = self.pieces_computer + self.pieces_player
            for domino in chose_from:
                if domino[0] == domino[1] and sum(domino) > biggest_value:
                    starting_domino, biggest_value = domino, sum(domino)

        # making first move
        if starting_domino in self.pieces_computer:
            self.pieces_computer.remove(starting_domino)
            self.turn = 'player'
        else:
            self.pieces_player.remove(starting_domino)
            self.turn = 'computer'

        self.line.append(starting_domino)

    def draw_interface(self):
        print('======================================================================')
        print(f'Stock size: {len(self.dominoes)}')
        print(f'Computer pieces: {len(self.pieces_computer)}')
        if len(self.line) < 7:
            print(f'\n{"".join(str(d) for d in self.line)}\n')
        else:
            print(f'\n{"".join(str(d) for d in self.line[0:3])}...{"".join(str(d) for d in self.line[-3:])}\n')
        print('Your pieces:')
        for n, p in enumerate(self.pieces_player, start=1):
            print(f'{n}:{p}')
        if self.turn == 'computer':
            print('\nStatus: Computer is about to make a move. Press Enter to continue...')
        else:
            print('\nStatus: It\'s your turn to make a move. Enter your command.')

    def check_winner(self):
        if not self.pieces_player:
            self.winner = 'player'
        elif not self.pieces_computer:
            self.winner = 'computer'
        else:
            snake = [n for d in self.line for n in d]
            if snake[0] == snake[-1]:
                if snake.count(snake[0]) == 8:
                    self.winner = 'draw'

    def print_winner(self):
        if self.winner == 'player':
            print('Status: The game is over. You won!')
        elif self.winner == 'computer':
            print('Status: The game is over. The computer won!')
        elif self.winner == 'draw':
            print('Status: The game is over. It\'s a draw!')
        else:
            print('Something went completely wrong')

    def make_player_move(self):
        while True:
            while True:
                try:
                    domino_index = int(input())
                    if abs(domino_index) not in range(0, len(self.pieces_player) + 1):
                        raise ValueError
                    break
                except ValueError:
                    print('Invalid input. Please try again.')
                    continue
            if domino_index != 0:
                index = abs(domino_index) - 1
                domino = self.pieces_player.pop(index)

                # processing move availability
                border = self.line[-1][-1] if domino_index > 0 else self.line[0][0]
                if domino[0] != border and domino[1] != border:
                    self.pieces_player.insert(index, domino)
                    print('Illegal move. Please try again.')
                    continue

                if domino[0] == border and domino_index < 0 or domino_index > 0 and domino[1] == border:
                    domino.reverse()

                self.line.append(domino) if domino_index > 0 else self.line.insert(0, domino)
                self.switch_turn()
                break
            else:
                if self.dominoes:
                    self.pieces_player.append(
                        self.dominoes.pop(self.dominoes.index(random.choice(self.dominoes))))
                    self.switch_turn()
                break

    def make_computer_move(self):
        input()
        self.switch_turn()

        # handling computer move
        borders = {'left': self.line[0][0], 'right': self.line[-1][-1]}
        for choice in self.pieces_computer:
            if any(b in borders.values() for b in choice):
                if choice[0] == borders['left'] or choice[1] == borders['left']:
                    if choice[0] == borders['left']:
                        choice.reverse()
                    self.line.insert(0, choice)
                    self.pieces_computer.remove(choice)
                else:
                    if choice[1] == borders['right']:
                        choice.reverse()
                    self.line.append(choice)
                    self.pieces_computer.remove(choice)
                break
        else:
            if self.dominoes:
                self.pieces_computer.append(self.dominoes.pop(self.dominoes.index(random.choice(self.dominoes))))

    def game_loop(self):
        while not self.winner:
            if self.turn == 'player':
                self.make_player_move()
            else:
                self.make_computer_move()
            self.check_winner()
            self.draw_interface()

    def play(self):
        self.setup_table()
        self.draw_interface()
        self.game_loop()
        self.print_winner()


DominoesGame().play()
