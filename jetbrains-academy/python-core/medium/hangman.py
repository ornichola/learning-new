import random
import string


WINS, LOSES = 0, 0
WORDS = ['python', 'java', 'swift', 'javascript']


def play():
    global WINS, LOSES
    word = random.choice(WORDS)
    mask = ['-' for _ in range(len(word))]
    guesses = list()
    attempts = 8
    while attempts:
        print('\n' + ''.join(mask))
        guess = input('Input a letter: ')
        if len(guess) != 1:
            print('Please, input a single letter.')
        elif guess not in string.ascii_lowercase:
            print('Please, enter a lowercase letter from the English alphabet.')
        elif guess in guesses:
            print('You\'ve already guessed this letter.')
        else:
            guesses.append(guess)
            if guess not in word:
                attempts -= 1
                print('That letter doesn\'t appear in the word.', f'# {attempts} attempts', sep='\n')
            else:
                for i, letter in enumerate(word, start=0):
                    if guess == letter:
                        mask[i] = guess

            if '-' not in mask:
                print(f'You guessed the word {word}!', 'You survived!', sep='\n')
                WINS += 1
                break
    else:
        print('You lost!')
        LOSES += 1


def show_score():
    print(f'You won: {WINS} times', f'You lost: {LOSES} times', sep='\n')


print('H A N G M A N')
while True:
    mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if mode not in ('play', 'results', 'exit'):
        continue
    if mode == 'play':
        play()
    if mode == 'results':
        show_score()
    if mode == 'exit':
        break
