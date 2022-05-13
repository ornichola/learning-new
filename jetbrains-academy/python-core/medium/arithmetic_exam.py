import random

LEVELS = {'1': '1 - simple operations with numbers 2-9', '2': '2 - integral squares of 11-29'}
TASKS = 5


def prepare_level_one() -> dict:
    endpoints = (2, 9)
    ops = ('+', '-', '*')

    tasks = [
        f'{random.randint(*endpoints)} {random.choice(ops)} {random.randint(*endpoints)}' for _ in range(TASKS)
    ]
    return {t: eval(t) for t in tasks}


def prepare_level_two() -> dict:
    endpoints = (11, 29)
    t = {number: number ** 2 for number in [random.randint(*endpoints) for _ in range(TASKS)]}
    return {number: number ** 2 for number in [random.randint(*endpoints) for _ in range(TASKS)]}


def handle_input():
    while True:
        guess = input()
        if guess and guess.lstrip('-').isnumeric():
            return int(guess)
        print('Incorrect format.')


def play(tasks: dict) -> int:
    right_guesses = 0
    for task, solution in tasks.items():
        print(task)
        user_guess = handle_input()
        if user_guess == solution:
            print('Right!')
            right_guesses += 1
        else:
            print('Wrong!')
    return right_guesses


levels = {'1': prepare_level_one, '2': prepare_level_two}
while True:
    print('Which level do you want? Enter a number:')
    print(LEVELS['1'])
    print(LEVELS['2'])
    level = input()
    if level not in levels:
        print('Incorrect format.')
        continue
    break

points = play(levels[level]())
print(f'Your mark is {points}/{TASKS}. Would you like to save the result? Enter yes or no.')
if input().lower() in ('yes', 'y'):
    print('What is your name?')
    name = input()
    with open('results.txt', 'a') as f:
        f.write(f'{name}: {points}/{TASKS} in level {LEVELS[level]}.\n')
    print('The results are saved in "results.txt".')

"""
Afterword
After finishing this stage, you are totally free to improve the project in any way you like to make it a more 
convenient and useful tool.

You can add any features to your application. It will not be verified by tests, so there are no strict requirements.

Sample ideas:

Add a complex exam. Increase a difficulty level on the fly. For example, if a person passed the 1st level, 
start the 2nd one immediately.
You can add a correction level: store the tasks with wrong answers and give them next time.
Add more difficulty levels.
Track the time (read about Timer).
Write a more detailed report to a file with the results.
Show previous results inside the app (show lines from results.txt that contains the username)
Any other improvement that might be useful!
"""
