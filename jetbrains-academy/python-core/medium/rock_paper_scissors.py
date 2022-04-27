import os
import random


def get_player_name() -> str:
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    return name


def get_player_rating(player: str) -> int:
    rating = 0

    if os.path.exists('rating.txt'):
        with open('rating.txt') as f:
            players_ratings = f.read().splitlines()
            for pr in players_ratings:
                if player in pr:
                    rating = int(pr.replace(f'{player} ', ''))
                    break

    return rating


def get_playable_options() -> [str]:
    options = input()
    if not options:
        options = ['rock', 'paper', 'scissors']
    else:
        options = options.split(',')
    print('Okay, let\'s start')
    return options


def form_relations(option: str, options: [str]) -> dict:
    """
    :param option: for which we need to form relations for
    :param options: possible game options (IN SORTED INCREASING ORDER)
    :return: dict with winning and losing options according chosen
    """
    options_sorted = list()
    index = options.index(option)
    if index != len(options) - 1:  # check if chosen option is not last in list for avoiding IndexError
        for opt in options[options.index(option) + 1:]:
            options_sorted.append(opt)
    for opt in options[:options.index(option)]:
        options_sorted.append(opt)

    return {
        'loses_to': options_sorted[:(len(options_sorted) // 2)],
        'wins_to': options_sorted[(len(options_sorted) // 2):]
    }


player_name = get_player_name()
player_rating = get_player_rating(player_name)
playable_options = get_playable_options()

while True:
    choice_ai = random.choice(playable_options)
    choice = input()
    if choice == '!exit':
        print('Bye!')
        break
    elif choice == '!rating':
        print(f'Your rating: {player_rating}')
    elif choice not in playable_options:
        print('Invalid input')
    else:
        relations = form_relations(choice, playable_options)
        if choice == choice_ai:
            print(f'There is a draw ({choice_ai})')
            player_rating += 50
        elif choice_ai in relations['loses_to']:
            print(f'Sorry, but the computer chose {choice_ai}')
        elif choice_ai in relations['wins_to']:
            print(f'Well done. The computer chose {choice_ai} and failed')
            player_rating += 100
        else:
            print('Error')
