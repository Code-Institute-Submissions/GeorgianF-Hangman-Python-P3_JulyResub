#HANGMAN GAME
import random
import string
from constants import hangman_state_by_lives_left, WORDS, DRAWING

print(DRAWING)

def get_incomplete_word(used_letters, word):
    incomplete_word_list = [letter if letter in used_letters else '-' for letter in word]  # set the output in the terminal. Show the letter if it's in the set otherwise show "-"
    return ' '.join(incomplete_word_list)

def start_game():
    selected_word = random.choice(WORDS)
    set_of_letters = set(selected_word)  # set to store the letters from the random word
    set_alphabet = set(string.ascii_uppercase) # The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    used_letters = set()  # set to store the letters that the user has guessed and it won't allow him to reenter, print them to the console
    lives_left = len(hangman_state_by_lives_left) # The lives that the user will have

    while len(set_of_letters) > 0 and lives_left > 0:
        print('You have', lives_left, 'lives. Enter a letter and find the missing word:\n')
        print('The letters used so far:',' '.join(used_letters)) #join the letters used into a set

        incomplete_word = get_incomplete_word(used_letters, selected_word)

        print(hangman_state_by_lives_left[lives_left]) # import the hangman drawing and print them to the console
        print('Current word:', incomplete_word) #print the word

        guess = input('Guess a letter: ').upper()
        if guess in set_alphabet - used_letters:
            used_letters.add(guess)
            if guess in set_of_letters:
                set_of_letters.remove(guess)
                print('')
            else:
                lives_left = lives_left - 1
                print('\n Wrong!', guess, 'is not in the word.')

        elif guess in used_letters:
            print('\n Pay attention, you already gave that letter')

        else:
            print('\nDo you know what a letter is, right?')

    if lives_left == 0:
        print('\n You were hanged. The word was', selected_word)
        
        ask_if_play_again()
    else:
        print('Your are amazing, it was:', selected_word, '!!')

def ask_if_play_again():
    print('\n Do you want to play again? Y/N')
    user_input = input().upper()
    if user_input == "Y":
        start_game()
    elif user_input == "N":
        print("To bad, hang you some other time! Bye... \n")
    else:
        print("Bye Bye!\n")

def initialise_game():
  print("\n!!! Welcome to the Hangman Game !!!\n")
  print('"When Faced With Death, Who Should Live Versus Who Will Live Are Two Entirely Separate Things." - Jigsaw\n')
  print("The rules are simple: The computer chooses of a word and you will to try to guess what it is one letter at a time.\n")
  start_game()


def main():
    initialise_game()

if __name__ == "__main__":
    main() 