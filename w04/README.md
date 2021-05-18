# Jumper
Tension so thick you can cut it with a knife! <i>Jumper</i> seems like a pretty 
laid back game until it's not! The rules are simple. The jumper guesses letters, 
one at a time. If the letter's not in the puzzle, the parachute loses a line. 
Guessing continues until the puzzle is solved or, well, you know.

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. 
Open a terminal and browse to the project's root folder. Start the program by 
running the following command.
```
python3 jumper 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                        (project root folder)
+-- hunter                  (source code for game)
  +-- game                  (specific game classes)
  +-- __init__.py           (python package file)
  +-- __main__.py           (entry point for program)
  +-- Director              (Contols play of the game)
    +-- Console
    +-- Puzzle
    +-- Player
    +-- startGame()
    +-- doInputs()
    +-- doUpdates()
    +-- doOutputs()
  +-- Player                (Provides inputs and keeps track of mistakes)
    +-- num life
    +-- updateLife()        Get a letter from the user, pass it it to check guess,
                            and update life remaining
    +-- displayParachute()  Use life count to display parachute by calling write console.
  +-- Puzzle                (Generates word and handles user input)
    +-- str chosenWord
    +-- list correctList
    +-- checkGuess(char guess)  Update correctList to show letters from correct guesses, 
                            return boolean on if guess is correct or not.
    +-- displayCorrect()    Display a represntation of the correct guesses from from correctList
  +-- Console               (Baisc input/output to console)
    +-- getLetter(str prompt) Takes prompt and gets a single letter from the user.
    +-- writeConsole(str text) Takes text and writes it to console.
+-- README.md               (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* TODO: Add your names and emails here
