from game.library_sound import LibrarySound
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
    try:
      self._health = int(sprite.properties['health'])
    except:
      self._health = 100
    try:
      self._id = int(sprite.properties['id'])
    except:
      self._id = None
    self._items = []
    self._weapon_type = 'melee'
    self._item_switch_cooldown = 0
    self._item_attack_cooldown = 0
    self._health_use_cooldown = 0

  def get_health(self) -> int:
    return self._health

  def set_health(self, health:int):
    self._health = health

  def reset_health_use_cooldown(self):
    self._health_use_cooldown = 30
  
  def get_health_use_cooldown(self) -> int:
    return self._health_use_cooldown

  def get_reset_health_use_cooldown(self) -> int:
    return 30

  def reset_item_attack_cooldown(self):
    cooldown = self.get_item_of_slot('weapon')
    if cooldown:
      cooldown = cooldown.get_cooldown() * 60
    else:
      cooldown = 30
    self._item_switch_cooldown = cooldown
  
  def get_item_attack_cooldown(self) -> float:
    return self._item_switch_cooldown

  def get_weapon_cooldown(self) -> float:
    cooldown = self.get_item_of_slot('weapon')
    if cooldown:
      return cooldown.get_cooldown() * 60
    else:
      return 30
  
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
  
  def set_items(self, items:list):
    self._items = items

  def get_item_of_type(self, type:str) -> Item:
    items = self.get_items_of_type(type)
    if items:
      return items[0]
    else:
      return None

  def get_items_of_type(self, type:str) -> list[Item]:
    items = [item for item in self.get_items() if item.get_type() == type]
    if len(items) > 0:
      return items
    else:
      return None

  def get_item_of_slot(self, slot:str) -> Item:
    items = self.get_items_of_slot(slot)
    if items:
      return items[0]
    else:
      return None

  def get_items_of_slot(self, slot:str) -> list[Item]:
    items = [item for item in self.get_items() if item.get_slot() == slot]
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
    protection = self.get_items_of_slot('protection')
    if protection:
      for item in protection:
        damage -= item.get_protection()
    if damage > 0:
      self._health -= damage

  def add_health(self, health:int):
    self._health = min(self._health + health, 100)

  def update(self, sound:LibrarySound):
    self._item_switch_cooldown -= 1 * int(self._item_switch_cooldown != 0)
    self._item_attack_cooldown -= 1 * int(self._item_attack_cooldown != 0)
    self._health_use_cooldown  -= 1 * int(self._health_use_cooldown  != 0)
    if self._health <= 0:
      sound.play_sound('death')
      self.kill()