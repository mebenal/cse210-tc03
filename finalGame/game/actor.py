from game import constants
from game.item import Item

import arcade
from arcade import Sprite

class Actor(Sprite):
  """
  """

  def __init__(self, sprite:Sprite):
    super().__init__()
    self.__dict__ = sprite.__dict__.copy()
    self._health = int(sprite.properties['health'])
    self._items = []
    self._weapon_type = 'melee'
    self._item_switch_cooldown = 0
    self._item_attack_cooldown = 0

  def reset_item_attack_cooldown(self):
    cooldown = self.get_item_of_type('weapon')
    if cooldown:
      cooldown = cooldown.get_cooldown() * 60
    else:
      cooldown = 30
    self._item_switch_cooldown = cooldown
  
  def get_item_attack_cooldown(self) -> float:
    return self._item_switch_cooldown
  
  def can_attack(self) -> bool:
    return self.get_item_attack_cooldown() == 0
  
  def reset_item_switch_cooldown(self):
    self._item_switch_cooldown = 30
  
  def get_item_switch_cooldown(self) -> int:
    return self._item_switch_cooldown

  def can_switch_item(self) -> bool:
    return self.get_item_switch_cooldown() == 0

  def get_items(self) -> list:
    return self._items
  
  def get_item_of_type(self, type:str) -> Item:
    items = self.get_items_of_type(type)
    if items:
      return items[0]
    else:
      return None

  def get_items_of_type(self, type:str) -> list[Item]:
    items = [item for item in self.get_items() if item.get_slot() == type]
    if len(items) > 0:
      return items
    else:
      return None

  def remove_item(self, item:Item):
    if item != None:
      self._items.remove(item)

  def add_item(self, item:Item):
    self._items.append(item)

  def take_damage(self, damage:float):
    protection = self.get_items_of_type('protection')
    if protection:
      for item in protection:
        damage -= item.get_protection()
    if damage > 0:
      self._health -= damage

  def update(self):
    self._item_switch_cooldown -= 1 * int(self._item_switch_cooldown != 0)
    self._item_attack_cooldown -= 1 * int(self._item_attack_cooldown != 0)