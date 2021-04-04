# KNOWN ISSUES -> wrong initial positions of racers

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
    return _screen


def compute_racers(number_of_racers: int):
    number_of_racers = number_of_racers - 1
    racers = list()
    spacing_x = WIDTH // number_of_racers
    racers_colors = random.sample(COLORS, number_of_racers)
    for i, color in enumerate(racers_colors, start=1):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.penup()                                           # ?
        racer.setpos(
            x=-WIDTH // 2 + i * spacing_x,
            y=-HEIGHT // 2 + 20
        )
        racer.pendown()                                         # ?
        racer.left(90)
        racer.speed(0)
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
    # number_of_racers = get_number_of_racers()
    number_of_racers = 10
    screen = init_screen()
    winner = race(compute_racers(number_of_racers))
    print(f'{winner.color()[0].capitalize()} turtle wins!')
