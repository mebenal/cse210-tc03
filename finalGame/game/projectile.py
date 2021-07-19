from game.library_items import LibraryItems
import math
from game import constants
from game.actor import Actor

import arcade
from arcade import Sprite

class Projectile(Sprite):
  """
  """

  def __init__(self, x_pos:int, y_pos:int, target:str, damage:float, change_x:float, change_y:float, distance:float, angle:float, projectile_id:int, item_textures:LibraryItems):
    super().__init__(None, scale=2, image_x=0, image_y=0, image_width=16, image_height=16, center_x=x_pos, center_y=y_pos)
    self._set_texture2(item_textures.get_item_by_id(projectile_id))
    self._start_position = self.position
    self._target = target
    self._damage = damage
    self.change_x = change_x
    self.change_y = change_y
    self._distance = distance
    self.angle = ((-math.pi / 4) + angle) * 180 / math.pi

  def get_distance_traveled(self) -> float:
    return math.sqrt(math.pow(self._start_position[0] - self.position[0], 2) + math.pow(self._start_position[1] - self.position[1], 2))

  def has_traveled_distance(self) -> bool:
    return self._distance - self.get_distance_traveled() < 0

  def get_target(self) -> str:
    return self._target

  def kill(self, sprite:Actor=None):
    if sprite:
      sprite.take_damage(self._damage)
    super().kill()