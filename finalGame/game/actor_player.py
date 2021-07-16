from game import constants
from game.actor import Actor

from arcade import Sprite

class Player(Actor):
  """
  """

  def __init__(self, sprite:Sprite):
    """The class constructor."""
    super().__init__(sprite)
    self._set_scale(constants.CHARACTER_SCALING)
    self._item_switch_held = None
    self._item_drop_held = None
    self._attack_held = None

  def set_item_switch(self, key_pressed:bool):
    self._item_switch_held = key_pressed

  def get_item_switch(self) -> bool:
    return self._item_switch_held
  
  def set_item_drop(self, key_pressed:bool):
    self._item_drop_held = key_pressed

  def get_item_drop(self) -> bool:
    return self._item_drop_held

  def set_attack(self, key_pressed:bool):
    self._attack_held = key_pressed

  def get_attack(self) -> bool:
    return self._attack_held

 