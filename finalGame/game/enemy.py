import random
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

  def update(self):
    super().update()
    
    if self._move_behavior == 0:
      self.move_random()
    else:
      self.move_stop()

  def move_random(self):
    self.change_y = random.randint(-5,5)
    self.change_x = random.randint(-5,5)

  def move_stop(self):
    self.change_y = 0
    self.change_x = 0



  