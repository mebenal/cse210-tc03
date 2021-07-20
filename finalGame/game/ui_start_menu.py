from game.type_rectangle_dict import RectangleDict
from game.type_sprite_dict import SpriteDict
from arcade.sprite import Sprite
from game.type_text_dict import TextDict
from game import constants
import random

import arcade

from game.actor_player import Player
from game.type_text import Text


class UIStartMenu:
  """Points earned. The responsibility of Score is to keep track of the player's points.

  Stereotype:
    Information Holder

  Attributes: 
    _points (integer): The number of points the food is worth.
  """
  
  def __init__(self):
    """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
    Args:
      self (Score): an instance of Score.
    """
    self._text_elements: TextDict = { 'start' : { 'string'   : 'To start, press Enter.',
                                                  'color'    : arcade.color.BLACK,
                                                  'font_size': 24,
                                                  'start_x'  : None,
                                                  'start_y'  : None }}
    self._sprite_elements: SpriteDict = {}
    self._rectangle_elements: RectangleDict = { 'background' : None }
    
  def update(self, cast):
    player: Player = cast['player']
    viewport = arcade.get_viewport()

    width = (viewport[1] - viewport[0])
    height = (viewport[3] - viewport[2])

    center_x = viewport[0] + (width / 2)
    center_y = viewport[2] + (height / 2)

    self._rectangle_elements['background'] = arcade.create_rectangle_filled(center_x, center_y, width - 128, height - 128, (128, 128, 128, 192))
    self._text_elements['start']['start_x'] = center_x - 150
    self._text_elements['start']['start_y'] = center_y

  def get_text_elements(self) -> TextDict:
    return self._text_elements

  def get_sprite_elements(self) -> SpriteDict:
    return self._sprite_elements

  def get_rectangle_elements(self) -> RectangleDict:
    return self._rectangle_elements
       
    
    