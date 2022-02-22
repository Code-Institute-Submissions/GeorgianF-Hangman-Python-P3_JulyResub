import random
import string
from drawings import hangman_lives

WORDS = ('OVERUSED', 'EXPRESS', 'PLEASANT', 'SWALLOW', 'PROPERTY', 'ACQUITANCE', 'GRADUAL', 'CAPITAL', 'DETECTIVE', 'MEASURE', 'DISGRACE', 'CIGARETTE', 'CROSSING', 'MULTIMEDIA', 'VOLUNTEER', 'TRANSFORM')
WRONG = 0
print("\n!!! Welcome to the Hangman Game !!!\n")
print('"When Faced With Death, Who Should Live Versus Who Will Live Are Two Entirely Separate Things." - Jigsaw\n')
print("The rules are simple: The computer chooses of a word and you will to try to guess what it is one letter at a time.\n")


def hangman():
    word = random.choice(WORDS)
    set_of_letters = set(word)  # set to store the letters from the random word
    set_alphabet = set(string.ascii_uppercase) # The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    used_letters = set()  # set to store the letters that the user has guessed and it won't allow him to reenter, print them to the console
    lives = len(hangman_lives) # The lives that the user will have

    while len(set_of_letters) > 0 and lives > 0:
        print('You have', lives, 'lives. Enter a letter and find the missing word:\n')
        print('The letters used so far:',' '.join(used_letters)) #join the letters used into a set

        word_list = [letter if letter in used_letters else '-' for letter in word]  # what current word is (ie W - R D)
        print(hangman_lives[lives]) # import the hangman drawing
        print('Current word: ', ' '.join(word_list)) #print the word

        guess = input('Guess a letter: ').upper()
        if guess in set_alphabet - used_letters:
            used_letters.add(guess)
            if guess in set_of_letters:
                set_of_letters.remove(guess)
                print('')
            else:
                lives = lives - 1
                print('\n Wrong!', guess, 'is not in the word.')

        elif guess in used_letters:
            print('\n Pay attention, you already gave that letter')

        else:
            print('\nDo you know what a letter is, right?')

    if lives == 0:
        print('\n You were hanged. The word was', word)
    else:
        print('Your are amazing, it was:', word, '!!')

hangman()
