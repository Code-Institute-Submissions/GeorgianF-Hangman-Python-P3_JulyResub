import random
import string
import constants


def get_incomplete_word(used_letters, word):
    # Show the letter if it's in the set otherwise show "-"
    incomplete_word_list = [
        letter if letter in used_letters else '-' for letter in word
        ]
    return ' '.join(incomplete_word_list)


def start_game():
    selected_word = random.choice(constants.WORDS)
    # set to store the letters from the random word
    set_of_letters = set(selected_word)
    # The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    set_alphabet = set(string.ascii_uppercase)
    # store the guessed letters and don't allow to reenter
    used_letters = set()
    # The lives that the user will have
    lives_left = len(constants.hangman_state_by_lives_left)

    while len(set_of_letters) > 0 and lives_left > 0:
        print('You have', lives_left, 'lives.\n')
        # join the letters used into a set
        print('The letters used so far:', ' '.join(used_letters))

        incomplete_word = get_incomplete_word(used_letters, selected_word)

        # import the hangman drawing and print them to the console
        print(constants.hangman_state_by_lives_left[lives_left])
        print('Current word:', incomplete_word)  # print the word

        guess = input('Guess a letter: \n').upper()
        if guess in set_alphabet - used_letters:
            print(constants.GOOD_JOB, "\n", '"', guess, '"', "is in the word")
            used_letters.add(guess)
            if guess in set_of_letters:
                set_of_letters.remove(guess)
                print('')
            else:
                lives_left = lives_left - 1
                print(
                    '\n',
                    constants.WRONG,
                    "\n",
                    '"',
                    guess,
                    '"',
                    'is not good, try again\n')

        elif guess in used_letters:
            print('\n Pay attention, you already gave that letter \n')

        else:
            print(
                '\n',
                constants.INPUT_ERROR,
                'Do you know what a letter is, right? \n'
                )

    if lives_left == 0:
        print(
            '\n',
            constants.GAME_OVER,
            'You were hanged. The word was',
            selected_word
            )
        ask_if_play_again()
    else:
        print(constants.WINNER)
        print('Your are amazing, it was:', selected_word, '!!')
        ask_if_play_again()


def ask_if_play_again():
    print('Do you want to play again? Y/N \n')
    try:
        user_input = input().upper()
        if user_input == "Y":
            print('Game starting')
        elif user_input == "N":
            print("To bad, hang you some other time! Bye... \n")
        else:
            raise TypeError('Invalid input')
    except TypeError as e:
        print(constants.INPUT_ERROR, e)
        ask_if_play_again()


def initialise_game():
    print(constants.DRAWING)
    print("\n!!! Welcome to the Hangman Game !!!\n")
    print("Simple rules: Guess the word, one letter at a time.\n")
    print('Hangman Game is great!')
    print('It teaches us that by saying the wrong things')
    print('You can end someones life...\n')
    start_game()


def main():
    initialise_game()


if __name__ == "__main__":
    main()
