import random
import string
from drawings import hangman_lives

WORDS = ('OVERUSED', 'EXPRESS', 'PLEASANT', 'SWALLOW', 'PROPERTY', 'ACQUITANCE', 'GRADUAL', 'CAPITAL', 'DETECTIVE', 'MEASURE', 'DISGRACE', 'CIGARETTE', 'CROSSING', 'MULTIMEDIA', 'VOLUNTEER', 'TRANSFORM')
WRONG = 0
print("\n!!! Welcome to the Hangman Game !!!\n")
print('"When Faced With Death, Who Should Live Versus Who Will Live Are Two Entirely Separate Things." - Jigsaw\n')
print("The rules are simple: The computer chooses of a word and you will to try to guess what it is one letter at a time.\n")
