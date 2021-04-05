import random
import turtle


WIDTH, HEIGHT = 750, 750
COLORS = [
    'red',
    'green',
    'blue',
    'cyan',
    'magenta',
    'yellow',
    'black',
    'pink',
    'brown',
    'orange',
]


def get_number_of_racers():
    while True:
        _racers = input('Enter the number of racers (2-10): ')
        if not _racers.isdigit():
            print('Input is not a number. Try again!')
        else:
            _racers = int(_racers)
            if not 2 <= _racers <= 10:
                print('Invalid number of racers. Expect from 2 to 10.')
            else:
                return _racers


def init_screen() -> turtle.Screen:
    _screen = turtle.Screen()
    _screen.setup(WIDTH, HEIGHT)
    _screen.title('Turtle Racing')
    _screen.bgcolor('grey')
    return _screen


def compute_positions(number_of_racers) -> [dict]:
    positions = list()
    placing_start, placing_end = -WIDTH // 2 + WIDTH * 0.1, WIDTH // 2 - WIDTH * 0.1
    spacing_x = (placing_end - placing_start) // (number_of_racers - 1)
    for i in range(number_of_racers):
        positions.append({
            'x': placing_start + i * spacing_x,
            'y': -HEIGHT // 2 + 20,
        })
    return positions


def place_racers_at_positions(positions: [dict]):
    racers = list()
    racers_colors = random.sample(COLORS, len(positions))
    for color, position in zip(racers_colors, positions):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.penup()
        racer.setpos(**position)
        racer.left(90)
        racer.pendown()
        racers.append(racer)
    return racers


def race(racers: list[turtle.Turtle]):
    while True:
        for racer in racers:
            racer.forward(random.randint(1, 20))
            _, current_y = racer.pos()
            if current_y >= HEIGHT // 2 - 10:
                return racer


if __name__ == '__main__':
    screen = init_screen()
    winner = race(place_racers_at_positions(compute_positions(get_number_of_racers())))
    print(f'{winner.color()[0].capitalize()} turtle wins!')
