from game import constants
import arcade

class Player(arcade.Sprite):
  """
  """

  def __init__(self, sprite):
    """The class constructor."""
    super().__init__()
    self.__dict__ = sprite.__dict__.copy()
    self._set_scale(constants.CHARACTER_SCALING)
    self._health = int(sprite.properties['health'])
    self._items = []
    self._item_switch_held = None
    self._item_switch_cooldown = 0
    self._item_drop_held = None

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

  def set_item_switch(self, key_pressed):
    self._item_switch_held = key_pressed

  def get_item_switch(self):
    return self._item_switch_held
  
  def set_item_drop(self, key_pressed):
    self._item_drop_held = key_pressed

  def get_item_drop(self):
    return self._item_drop_held

  def update(self):
    self._item_switch_cooldown -= 1 * int(self._item_switch_cooldown != 0)