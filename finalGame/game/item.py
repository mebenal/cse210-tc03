from game import constants
import arcade

class Item(arcade.Sprite):
  def __init__(self, sprite):
    """The class constructor."""
    super().__init__()
    self.__dict__ = sprite.__dict__.copy()
    self._set_scale(constants.ITEM_SCALING)
    self._slot = sprite.properties['slot']
    if self._slot == 'weapon':
      self._range = int(sprite.properties['range'])
      self._damage = int(sprite.properties['damage'])
    else:
      self._protection = int(sprite.properties['protection'])

  def get_slot(self):
    return self._slot

  def get_damage(self):
    return self._damage