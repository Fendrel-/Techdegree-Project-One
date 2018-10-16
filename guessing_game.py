"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random


def start_game():
    def game_loop():
        counter = 1
        playing = True
        while playing:
            try:
                guess = int(input('\nPick a number between 1 and 100\n>>> '))
                if guess in range(1, 101):
                    if guess > random_number:
                        print('\nSorry that\'s incorrect.')
                        print('The number I\'m thinking of is lower than that.')
                        counter += 1
                    elif guess < random_number:
                        print('\nSorry that\'s incorrect.')
                        print('The number I\'m thinking of is higher than that.')
                        counter += 1
                    else:
                        print('\nYou got it!')
                        print('That was the number I was thinking of!\n')
                        print('You guessed the number in {} tries.'.format(counter))
                        playing = False
                else:
                    raise ValueError
            except ValueError as error:
                print('\nSorry that\'s not a valid input. Try again.')
        return counter


    random_number = random.randint(1, 100)
    num_guesses = game_loop()
    return num_guesses

def best_score(num_guesses):
    global high_score
    if num_guesses < high_score:
        print('\nCongrats! You got a high score!')
        print('Previous high score (least guesses) was {}.'.format(high_score))
        return num_guesses
    else:
        print('\nThe current high score (least guesses) is {}.'.format(high_score))
        return high_score


def new_game():
    play_again = False
    while play_again is False:
        try:
            choice = input('\nWould you like to play again? (Y)es/(N)o\n>>> ')
            if choice.upper() in ['NO', 'N']:
                print('\nThank you for playing!')
                exit()
            elif choice.upper() in ['YES', 'Y']:
                play_again = True
            else:
                raise ValueError
        except ValueError as error:
            print('\nI\'m sorry, I don\'t understand that.')


if __name__ == '__main__':
    print('Hello and Welcome to the Number Guessing Game!')
    global high_score
    while True:
        num_guesses = start_game()
        try:
            high_score = best_score(num_guesses)
        except NameError:
            print('Congrats! You got a high score!')
            high_score = num_guesses
        new_game()
