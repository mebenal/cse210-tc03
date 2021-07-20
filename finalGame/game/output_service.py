from game.ui_game import UIGame
from game import constants
from game.type_map_dict import MapDict

import sys
import math
import arcade
from arcade import SpriteList

class OutputService:
  """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
  Stereotype: 
    Service Provider

  Attributes:
    _screen (Screen): An Asciimatics screen.
  """

  def __init__(self):
    """The class constructor.
       
    Args:
      screen (Screen): An Asciimatics Screen.
    """
    return
        
  def draw_layer(self, layer:SpriteList):
    """Renders the given actor's text on the screen.

    Args:
      actor (Actor): The actor to render.
    """ 
    layer.draw(filter='')

  def draw_layers(self, layers:MapDict, drawOrder:list[str]):
    """Renders the given list of actors on the screen.

    Args:
      actors (list): The actors to render.
    """ 
    for name in drawOrder:
      self.draw_layer(layers[name])

  def draw_ui(self, ui:UIGame):
    rectangles = ui.get_rectangle_elements()
    for i in constants.RECTANGLE_ORDER:
      try:
        rectangles[i].draw()
      except:
        pass
    for i, (key, text) in enumerate(ui.get_text_elements().items()):
      if text['start_x']:
        arcade.draw_text(text['string'], text['start_x'], text['start_y'], text['color'], text['font_size'])
    for i, (key, sprite) in enumerate(ui.get_sprite_elements().items()):
      if sprite:
        sprite.draw()
    