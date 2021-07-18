from game.type_rectangle_dict import RectangleDict
from game.type_sprite_dict import SpriteDict
from arcade.sprite import Sprite
from game.type_text_dict import TextDict
from game import constants
import random

import arcade

from game.actor_player import Player
from game.type_text import Text


class UI:
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
    self._text_elements: TextDict = { 'hp' : { 'string'   : 'HP:',
                                               'color'    : arcade.color.BLACK,
                                               'font_size':12 } }
    self._sprite_elements: SpriteDict = {'player_weapon':None}
    self._rectangle_elements: RectangleDict = { 'player_weapon_cooldown' : None,
                                                'player_health_bar'      : None,
                                                'player_health_outline'  : None}
    
  def update(self, cast):
    player: Player = cast['player']
    viewport = arcade.get_viewport()

    screen_bottom_offset = viewport[2] + 32
    screen_left_offset = viewport[0] + 32
    player_top_offset = player.position[1] + 32
    sprite_scaling = constants.ITEM_SCALING
    cooldown = player.get_item_attack_cooldown() / player.get_weapon_cooldown()
    health_ratio = player.get_health() / 100
    sprite_size = sprite_scaling * 16

    self._rectangle_elements['player_health_outline'] = arcade.create_rectangle_filled(player.position[0], player_top_offset, sprite_size * 1.5, sprite_size / 3, (128, 128, 128, 255))
    self._rectangle_elements['player_health_bar']     = arcade.create_rectangle_filled(player.position[0] - .75 * sprite_size + .75 * sprite_size * health_ratio, player_top_offset, sprite_size * health_ratio * 1.5, sprite_size / 3, (255, 0, 0, 255))
    self._text_elements['hp']['start_x'] = player.position[0] - 50
    self._text_elements['hp']['start_y'] = player.position[1] + 24
    
    
    if player.get_item_of_type('weapon') != None:
      weapon = Sprite(None, sprite_scaling, 0, 0, sprite_size, sprite_size, screen_left_offset, screen_bottom_offset)
      weapon._set_texture2(player.get_item_of_type('weapon')._get_texture())
      self._sprite_elements['player_weapon'] = weapon
    else:
      self._sprite_elements['player_weapon'] = None

    self._rectangle_elements['player_weapon_cooldown'] = arcade.create_rectangle_filled(screen_left_offset, screen_bottom_offset - .5 * sprite_size + sprite_size * cooldown * .5, sprite_size, sprite_size * cooldown, (128, 128, 128, 192))

  def get_text_elements(self) -> TextDict:
    return self._text_elements

  def get_sprite_elements(self) -> SpriteDict:
    return self._sprite_elements

  def get_rectangle_elements(self) -> RectangleDict:
    return self._rectangle_elements
       
    
    