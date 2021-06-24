from game import constants
import arcade

class Enemy(arcade.Sprite):
  def __init__(self, sprite):
    """The class constructor."""
    super().__init__()
    self.__dict__ = sprite.__dict__.copy()
    self._set_scale(constants.CHARACTER_SCALING)
    self._move_behavior = 0

  def set_move_behavior(self, new_behavior):
    self._move_behavior = new_behavior

  