from game import constants

import arcade
from arcade import Sprite

class Item(Sprite):
  def __init__(self, sprite):
    """The class constructor."""
    super().__init__()
    self.__dict__ = sprite.__dict__.copy()
    self._set_scale(constants.ITEM_SCALING)
    try:
      self._slot = sprite.properties['slot']
      self._type = sprite.properties['type']
      self._id   = sprite.properties['id']
      if self._slot == 'weapon':
        if self._type == 'ranged':
          self._projectile_id = int(sprite.properties['projectile_id'])
        self._range = float(sprite.properties['range'])
        self._damage = float(sprite.properties['damage'])
        self._cooldown = float(sprite.properties['cooldown'])
      elif self._slot != 'special':
        self._protection = int(sprite.properties['protection'])
      elif self._slot == 'special':
        if self._type == 'health':
          self._health = int(sprite.properties['health'])
    except:
      self.slot = 'invaild'
      self.type = 'invalid'

  def get_slot(self) -> str:
    return self._slot

  def get_type(self) -> str:
    return self._type

  def get_range(self) -> int:
    return self._range

  def get_cooldown(self) -> int:
    return self._cooldown

  def get_damage(self) -> int:
    return self._damage

  def get_protection(self) -> int:
    return self._protection 
  
  def get_projectile_id(self) -> int:
    return self._projectile_id

  def get_health(self) -> int:
    return self._health