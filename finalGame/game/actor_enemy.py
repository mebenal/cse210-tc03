from game.actor_walking_animated import ActorWalkingAnimated
from game import constants
from game.actor import Actor

import math
import random
import arcade
from arcade import SpriteList
from arcade import Sprite
from typing import Iterable


class Enemy(ActorWalkingAnimated):
  def __init__(self, sprite:Sprite):
    """The class constructor."""
    super().__init__(sprite)
    self._set_scale(constants.CHARACTER_SCALING)
    self._move_behavior = 0
    self._distance = 0
    

  def set_move_behavior(self, new_behavior:int):
    self._move_behavior = new_behavior

  def update_movement(self, frame_count:int, collision:SpriteList, position:list[float,float]):
    past_position = self.position
    moved = False

    if self._move_behavior == 1:
      self.move_towards_point(position)
      moved = True
    elif self._move_behavior == 2:
      self.move_away_point(position)
      moved = True
    elif self._move_behavior == 0 and frame_count % 60 == 0:
      self.move_random()
      moved = True
    elif self._move_behavior == 0 and frame_count % 20 != 0:
      pass
    else:
      self.move_stop()
    
    self.position = [self._position[0] + self.change_x, self._position[1] + self.change_y]
    self.angle += self.change_angle

    if moved:
      if len(arcade.check_for_collision_with_list(self, collision)) != 0:
        self.position = past_position
        self.change_x = self.change_y = 0

  def move_random(self):
    angle = random.randint(0, 359) * math.pi / 180
    self.change_x = constants.ENEMY_MOVEMENT_SPEED * math.cos(angle)
    self.change_y = constants.ENEMY_MOVEMENT_SPEED * math.sin(angle)

  def move_stop(self):
    self.change_y = 0
    self.change_x = 0

  def move_towards_point(self, point:list[float,float]):
    angle = self.get_angle_to_point(point)
    self.change_x = constants.ENEMY_MOVEMENT_SPEED * math.cos(angle)
    self.change_y = constants.ENEMY_MOVEMENT_SPEED * math.sin(angle)

  def move_away_point(self, point:list[float,float]):
    self.move_towards_point(point)
    self.change_x *= -1
    self.change_y *= -1

  def get_angle_to_point(self, point:list[float,float]) -> float:
    x = point[0] - self.position[0]
    y = point[1] - self.position[1]
    angle = math.atan2(y, x)
    return angle

  def set_distance_to_player(self, distance:float):
    self._distance = distance

  def get_distance_to_player(self) -> float:
    return self._distance