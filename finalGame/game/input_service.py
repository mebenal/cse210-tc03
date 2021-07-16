from game import constants
from game.actor_player import Player

import arcade

class InputService:
  """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

  Stereotype: 
    Service Provider

  Attributes:
    _keys (list): Points for up, dn, lt, rt.
  """

  def __init__(self):
    """The class constructor."""
    self._keys = []

  def set_key(self, key, modifiers):
    #Ignoring modifies ar this point...
    self._keys.append(key)

  def remove_key(self, key, modifiers):
    self._keys.remove(key)

  def set_direction(self, player:Player):
    if any(item in [arcade.key.UP, arcade.key.W] for item in self._keys):
      player.change_y = constants.PLAYER_MOVEMENT_SPEED
    elif any(item in [arcade.key.DOWN, arcade.key.S] for item in self._keys):
      player.change_y = -constants.PLAYER_MOVEMENT_SPEED
    else:
      player.change_y = 0

    if any(item in [arcade.key.LEFT, arcade.key.A] for item in self._keys):
      player.change_x = -constants.PLAYER_MOVEMENT_SPEED
    elif any(item in [arcade.key.RIGHT, arcade.key.D] for item in self._keys):
      player.change_x = constants.PLAYER_MOVEMENT_SPEED
    else:
      player.change_x = 0
  
  def update_options(self, player:Player):
    player.set_item_switch(arcade.key.E in self._keys)
    player.set_item_drop(arcade.key.Q in self._keys)
    player.set_attack(arcade.key.SPACE in self._keys)