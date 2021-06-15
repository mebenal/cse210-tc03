# Bullet Destiny
Kill stuff. Nuff said.

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
python3 batter 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- finalGame              (source code for game)
  +-- game              (specific game classes)
    +-- Action
      +-- execute()
    +-- Actor
      +-- _image_set      list
      +-- _current_image  Image
      +-- _position       Point
      +-- _velocity       Point
      +-- _team           int
      +-- _health         int
      +-- _equipment      list
      +-- get_position()
      +-- get_current_image()
      +-- get_velocity()
      +-- get_health()
      +-- get_team()
      +-- get_equipment()
      +-- set_position()
      +-- set_velocity()
      +-- set_team()
      +-- add_equipment()
      +-- remove_equipment()
      +-- update_health()
      +-- next_image()
    +-- Armor
      +-- _protection
      +-- get_protection()
      +-- set_protection()
    +-- Background
      +-- _text_board
      +-- _image_list
      +-- _backround_frame
      +-- construct_frame()
    +-- Constants
    +-- ControlActorsAction(Action)
      +-- execute(cast)
    +-- Counter(Actor)
      +-- _count
      +-- add()
      +-- subtract()
    +-- Director
      +-- start_game()
      +-- _cue_action()
    +-- DrawActorsAction(Action)
      +-- execute(cast)
    +-- Equipment
      +-- _type
      +-- get_type()
      +-- remove()
    +-- HandleCollisionsAction(Action)
      +-- execute(cast)
    +-- InputService
      +-- _screen
      +-- _keys       Dict
      +-- get_direction()
    +-- MoveActorsAction(Action)
      +-- execute(cast)
      +-- move_actor()
    +-- OutputService
      +-- _screen
      +-- clear_screen()
      +-- draw_actor()
      +-- draw_actors()
      +-- flush_buffer()
    +-- Point
      +-- _x
      +-- _y
      +-- add(Point)
      +-- equals(Point)
      +-- get_x()
      +-- get_y()
      +-- is_zero()
    +-- Weapon
      +-- _damage
      +-- _range
      +-- _speed
      +-- damage_actor()
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* 

## Authors
---
* # TODO: Add your names and emails here
