# The Hangman Game
* History: Though the origins of the game are unknown, a variant is mentioned in a book of children's games assembled by * *Alice Gomme* * in * *1894* * called * *Birds, Beasts, and Fishes* * . This version lacks the image of a hanged man, instead relying on keeping score as to the number of attempts it took each player to fill in the blanks.

## Main introduction into the game

* This is a word guessing game, where the user enters one letter each time until the word is complete.
* When the game is run the user will be greated with an ASCII image (* *to give a retro 90' look* * ) and a message
  **
* The user is explained the rules of the game
* The user has 7 lives to start with ( * ***as in lucky no. 7*** * ), each fault decreases the lives number and until the user is "hanged"
* The word is randomly chosen from a predefined list, that can be found on the constants.py document
* 
<img width="446" alt="intro" src="https://user-images.githubusercontent.com/91877102/160243273-d2193db9-bdb5-4df5-bc83-04f00fe64ced.png">


## How to use it?

### Deployment
- The app is deployed with Heroku and the link is found here: https://hangman-game-ci-p3.herokuapp.com/ -> Click the _Run_ button
- The Github Link: https://github.com/GeorgianF/Hangman-Python-P3

### Functionality
- For the logic of the the game I have redacted the following flow chart:

<img width="633" alt="Screenshot 2022-03-26 at 20 30 49" src="https://user-images.githubusercontent.com/91877102/160254483-359ffcb3-2300-4ed2-b165-693c18dbf721.png">

- The user enters one letter each time and checks if the input is found in the random generated word
- If it's found, it will populate the word 

<img width="268" alt="guess the word" src="https://user-images.githubusercontent.com/91877102/160243796-25e1faa2-8d8f-4010-bb09-454797ecc0fd.png">

- If it's not found, it will populate a list of used letters, so the user can keep track of the entered letters. Also the console displays the message _"Wrong! - is not in the word."_

<img width="254" alt="wrong guess" src="https://user-images.githubusercontent.com/91877102/160243808-d8ceabbe-92d2-4e0b-9424-4b503ae85ec6.png">

- If the counter reaches 0 - the last image it's imported and the user is _"hanged"_

<img width="300" alt="hanged" src="https://user-images.githubusercontent.com/91877102/160243823-46da9a4a-a212-451b-80e6-d297d9730ce7.png">

- If the word is completed, the user it's congratulated with the message _"Your are amazing, it was: WORD"_

<img width="275" alt="word right" src="https://user-images.githubusercontent.com/91877102/160243837-79e3b494-07af-4dd7-822b-7bfae25f45c3.png">

At the end, the user it's asked if he wants to play again. He must enter _Y_ or _N_.

- If the user chooses _N_ the game will stop

<img width="307" alt="end game" src="https://user-images.githubusercontent.com/91877102/160243999-97dfab2b-0b6d-4566-9f97-933c764c252a.png">

- If the user chooses _Y_ the game will restart with another random word
- If the user chooses empty or invalid data, the question to play again will repeat - it will accept only Y or N

<img width="225" alt="wrong input end game" src="https://user-images.githubusercontent.com/91877102/160244128-dca65423-629d-4948-b84e-524ef2acd68c.png">

### Restriction
The user can't enter numbers or more than one letter at the time, it will print the message _"Do you know what a letter is, right?"_
It won't take a _"live"_ if the input is wrong

<img width="276" alt="wrong input" src="https://user-images.githubusercontent.com/91877102/160244154-c07086b7-18b5-4675-a78a-aaa353959398.png">

## Testing
- I've tested the game for functionality in all the stages mentioned above and verified all the functions.
- Tested the deployed game in the browsers: Safari, Chrome, Edge

## Validator Testing 
Tested the code on http://pep8online.com/ with no errors

### Document run.py:

<img width="966" alt="run" src="https://user-images.githubusercontent.com/91877102/160244308-28513e06-ac11-4d76-a65c-6bef0b040684.png">

### Document constants.py:

<img width="975" alt="constants" src="https://user-images.githubusercontent.com/91877102/160244329-53414c2a-7f35-4942-bcc9-93849941977b.png">

## Unfixed Bugs
No unfixed bugs

## Credits

- Kylie Ying: https://github.com/kying18/hangman
- Kylie Ying: https://www.youtube.com/watch?v=8ext9G7xspg&t=1572s
- https://docs.python.org/3/library/random.html
- https://docs.python.org/3/library/string.html
- Book: Python Programming Third Edition. Author: Michael Dawson
- I've used the online random word generator: https://randomwordgenerator.com/
- ASCII image generator https://fsymbols.com/generators/carty/







