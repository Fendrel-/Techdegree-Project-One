"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
For this first project we will be using Workspaces.
NOTE: If you strongly prefer to work locally on your own computer,
you can totally do that by clicking: File -> Download Workspace in
the file menu after you fork the snapshot of this workspace.
"""

import random


def start_game():
    """Psuedo-code Hints
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player
      "It's lower".
      b. If the guess is less than the solution, display to the player
      "It's higher".
    4. Once the guess is correct, stop looping, inform the user they
    "Got it" and show how many attempts it took them to get the
    correct number.
    5. Let the player know the game is ending, or something that
    indicates the game is over.
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    def game_loop():
        def best_score(num_guesses):
            global high_score
            if num_guesses < high_score:
                print('Congrats! You got a high score!')
                print('Previous high score was {}.'.format(high_score))
                high_score = num_guesses
            else:
                print('The current high score is {}.'.format(high_score))

        counter = 1
        playing = True
        while playing:
            guess = int(input('Pick a number between 1 and 10 '))
            if guess not in range(1, 11):
                print('Sorry that\'s not a valid input. Try again.')
            elif guess > random_number:
                print('Sorry that\'s incorrect.')
                print('The number I\'m thinking of is lower than that.')
                counter += 1
            elif guess < random_number:
                print('Sorry that\'s incorrect.')
                print('The number I\'m thinking of is higher than that.')
                counter += 1
            else:
                print('You got it!')
                print('That was the number I was thinking of!')
                print('You guessed the number in {} tries.'.format(counter))
                playing = False
        best_score(counter)

    random_number = random.randint(1, 10)
    game_loop()

def new_game():
    if input('Would you like to play again? (Yes/No)').upper() == 'NO':
        exit()

if __name__ == '__main__':
    global high_score
    high_score = 11
    print('Hello and Welcome to the Number Guessing Game!')
    while True:
        start_game()
        new_game()

