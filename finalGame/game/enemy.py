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
    self._health = int(sprite.properties['health'])
    self._items = []
    self._item_switch_cooldown = 0

  def reset_item_switch_cooldown(self):
    self._item_switch_cooldown = 30
  
  def get_item_switch_cooldown(self):
    return self._item_switch_cooldown

  def get_items(self):
    return self._items

  def remove_item(self, item):
    if item != None:
      self._items.remove(item)

  def add_item(self, item):
    self._items.append(item)

  def set_move_behavior(self, new_behavior):
    self._move_behavior = new_behavior

  def update_movement(self, frame_count, collision):
    past_position = self.position
    
    if frame_count % 20 != 0:
      pass
    elif self._move_behavior == 0 and frame_count % 60 == 0:
      self.move_stop()
    else:
      self.move_random()
    
    super().update()
    
    if len(arcade.check_for_collision_with_list(self,collision)) > 0:
      self.position = past_position
      self.change_x = self.change_y = 0


  def move_random(self):
    self.change_y = random.randint(-5,5)
    self.change_x = random.randint(-5,5)

  def move_stop(self):
    self.change_y = 0
    self.change_x = 0



  