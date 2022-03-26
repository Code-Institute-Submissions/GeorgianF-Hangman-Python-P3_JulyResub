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


## Functionality of the game

- The game imports images of the hangman from a separate file and corelates them with the lives left.
- The user enters one letter each time and checks if the input is found in the random generated word
- If it's found, it will populate the word 
- If it's not found, it will populate a list of used letters, so the user can keep track of the entered letters. Also the console displays the message _"Wrong! - is not in the word."_
- If the counter reaches 0 - the last image it's imported and the user is _"hanged"_
- If the word is completed, the user it's congratulated with the message _"Your are amazing, it was: WORD"_

At the end, the user it's asked if he wants to play again. He must enter _Y_ or _N_.
If he enters anything else that the two letters, the game will stop with the message "Bye Bye!!"

<img width="418" alt="Screenshot 2022-02-26 at 20 16 48" src="https://user-images.githubusercontent.com/91877102/155856243-654bf0be-97b0-41a6-a5e7-35e79cbec413.png">

## Restriction
The user can't enter numbers or more than one letter at the time, it will throw a error message _"Do you know what a letter is, right?"_

## Deployment
- The app is deployed with Heroku and the link is found here: https://hangman-game-ci-p3.herokuapp.com/
- The Github Link: https://github.com/GeorgianF/Hangman-Python-P3

## Testing
- I've tested the game and verified all the functions.
- Tested the deployed game in the browsers: Safari, Chrome, Edge

When I first deployed the game, it gave an error due to the fact that I forgot to add the config var PORT 8000. I had to delete the the app and redeploy.

## Validator Testing 
Tested the code on http://pep8online.com/ with no errors

<img width="430" alt="Screenshot 2022-02-26 at 18 20 37" src="https://user-images.githubusercontent.com/91877102/155856061-3fa50d04-e31f-477a-847e-a8f8fc297bb2.png">

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







