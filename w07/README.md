# Speed
Think you can type faster than your peers? Start a <i>Speed</i> 
tournament and you'll know! The rules are simple. Type the words you 
see as they move across the screen. Press enter to clear the buffer at 
any time. Type a word correctly and your score goes up.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and asciimatics 1.12.0 or new installed 
and running on your machine. You can install Asciimatics by opening a terminal 
and running the following command.
```
python3 -m pip install asciimatics
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running the following command.
```
python3 speed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- speed               (source code for game)
  +-- game              (specific game classes)
    +-- Director
      +-- _keep_playing
      +-- _input_service
      +-- _output_service
      +-- _score
      +-- _buffer
      +-- _words
      +-- start_game()
      +-- _do_inputs()
      +-- _do_updates()
      +-- _do_outputs()
      +-- _handle_word_reset()
    +-- Actor
      +-- _text
      +-- _position
      +-- _velocity
      +-- get_position()
      +-- get_text()
      +-- get_velocity()
      +-- move_next()
      +-- set_position(Point)
      +-- set_text(String)
      +-- set_velocity(Point)
    +-- Score(Actor)
      +-- _points
      +-- add_points(int)
    +-- Buffer(Actor)
      +-- _player_input             String storing the users input
      +-- check_word(String)        Checks player_input against the parameter and returns a boolean value
      +-- get_player_input()        Returns the value of player input
      +-- set_player_input(String)  Sets the player_input to the parameter
      +-- reset()                   Sets player_input to an empty string
    +-- Word(Actor)
      +-- _word         Current word selected from the LIBRARY constant
      +-- reset_word()  Changes the word to a new word  
    +-- Input_Service
      +-- _screen
      +-- get_letter()
    +-- Output_Service
      +-- _screen
      +-- clear_screen()
      +-- draw_actor(Actor)
      +-- draw_actors(List)
      +-- flush_buffer()
    +-- Point
      +-- _x
      +-- _y
      +-- add(Point)
      +-- equals(Point)
      +-- get_x()
      +-- get_y()
      +-- reverse()
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Asciimatics 1.12.0

## Authors
---
* # TODO: Add names and emails here
