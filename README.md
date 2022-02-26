# The Hangman Game

<img width="575" alt="Screenshot 2022-02-26 at 18 17 15" src="https://user-images.githubusercontent.com/91877102/155855132-547b7ed9-db12-4305-a41c-fd2c5aef57c3.png">

* This is a word guessing game, where the user enters one letter each time until the word is complete.
* The user has 7 lives to start with, each fault decreses the lives number and until the user is "hanged"
* The word is randomly choosed from a predefined list.

## Main introduction into the game

- Whe the game is run the user will be greated with an ASCII image (to give a retro look) and a message
- The user is explained the rules of the game
- The starting counter of the available lives is displayed (7 lives)

## Functionality of the game

- The game imports images of the hangman from a separate folder and an corelated with the lives left.
- The user enters one letter each time and the check is the input is found in the random generated word
- If it's found, it will populate the word 
- If it's not found, it will populate a list of user words, so the user can keep track of the entered words. Also the console displays the message _"Wrong! Q is not in the word."_
- If the counter reaches 0 - the last image it's imported and the user is "hanged"
- If the word is completed, the user it's congratulated with the message _"Your are amazing, it was: WORD"_

At the end, the user it's asked if he wants to play again. He must enter _Y_ or _N_.
If he enters anything else that the two letters, the game will stop with the message "Bye Bye!!"

<img width="418" alt="Screenshot 2022-02-26 at 20 16 48" src="https://user-images.githubusercontent.com/91877102/155856243-654bf0be-97b0-41a6-a5e7-35e79cbec413.png">

## Restriction
The user can't enter numbers or more than one letter at the time, it will throw a error message _"Do you know what a letter is, right?"_

## Deployment
- The apps is deployed with Heroku and the link is found here: https://hangman-game-ci-p3.herokuapp.com/
- The Github Link: https://github.com/GeorgianF/Hangman-Python-P3

## Testing
- I've tested the game and verified all the functions.
- Tested the deployed game in the browsers: Safari, Chrome, Edge

When first deploying the game, it gave an error due to the fact that I forgot to add the config var PORT 8000. I had to delete the the app and redeploy.

## Validator Testing 
Tested the code on http://pep8online.com/ with no errors

<img width="430" alt="Screenshot 2022-02-26 at 18 20 37" src="https://user-images.githubusercontent.com/91877102/155856061-3fa50d04-e31f-477a-847e-a8f8fc297bb2.png">

### Unfixed Bugs
No unfixed bugs






