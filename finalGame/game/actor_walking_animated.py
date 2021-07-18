from game.load_animation_textures import LoadAnimationTextures
from game.actor import Actor
from game import constants
from typing import List
from arcade import Texture
import math

class ActorWalkingAnimated(Actor):
  def __init__(self, sprite):
    super().__init__(sprite)
    self.state = constants.FACE_RIGHT
    self.stand_right_textures: List[Texture] = []
    self.stand_left_textures: List[Texture] = []
    self.stand_up_textures: List[Texture] = []
    self.stand_down_textures: List[Texture] = []
    self.walk_left_textures: List[Texture] = []
    self.walk_right_textures: List[Texture] = []
    self.walk_up_textures: List[Texture] = []
    self.walk_down_textures: List[Texture] = []
    self.cur_texture_index = 0
    self.texture_change_distance = 20
    self.last_texture_change_center_x = 0
    self.last_texture_change_center_y = 0

  def update_animation(self, delta_time: float = 1/60):
    """
    Logic for selecting the proper texture to use.
    """
    x1 = self.center_x
    x2 = self.last_texture_change_center_x
    y1 = self.center_y
    y2 = self.last_texture_change_center_y
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    texture_list: List[Texture] = []

    change_direction = False
    if self.change_x > self.change_y \
       and self.change_x > 0 \
       and len(self.walk_right_textures) > 0:
      self.state = constants.FACE_RIGHT
      if self.state != constants.FACE_RIGHT:
        change_direction = True
    elif self.change_x < self.change_y and self.change_x < 0 \
         and len(self.walk_left_textures) > 0:
      self.state = constants.FACE_LEFT
      if self.state != constants.FACE_LEFT:
          change_direction = True
    elif self.change_y <= self.change_x and self.change_y < 0 \
         and len(self.walk_down_textures) > 0:
      self.state = constants.FACE_DOWN
      if self.state != constants.FACE_DOWN:
          change_direction = True
    elif self.change_y >= self.change_x and self.change_y > 0 \
         and len(self.walk_up_textures) > 0:
      self.state = constants.FACE_UP
      if self.state != constants.FACE_UP:
          change_direction = True

    if self.change_x == 0 and self.change_y == 0:
      if self.state == constants.FACE_LEFT:
        self.texture = self.stand_left_textures[0]
      elif self.state == constants.FACE_RIGHT:
        self.texture = self.stand_right_textures[0]
      elif self.state == constants.FACE_UP:
        self.texture = self.stand_up_textures[0]
      elif self.state == constants.FACE_DOWN:
        self.texture = self.stand_down_textures[0]

    elif change_direction or distance >= self.texture_change_distance:
      self.last_texture_change_center_x = self.center_x
      self.last_texture_change_center_y = self.center_y

      if self.state == constants.FACE_LEFT:
        texture_list = self.walk_left_textures
        if texture_list is None or len(texture_list) == 0:
          raise RuntimeError("update_animation was called on a sprite that doesn't have a "
                             "list of walk left textures.")
      elif self.state == constants.FACE_RIGHT:
        texture_list = self.walk_right_textures
        if texture_list is None or len(texture_list) == 0:
          raise RuntimeError("update_animation was called on a sprite that doesn't have a list of "
                             "walk right textures.")
      elif self.state == constants.FACE_UP:
        texture_list = self.walk_up_textures
        if texture_list is None or len(texture_list) == 0:
          raise RuntimeError("update_animation was called on a sprite that doesn't have a list of "
                             "walk up textures.")
      elif self.state == constants.FACE_DOWN:
        texture_list = self.walk_down_textures
        if texture_list is None or len(texture_list) == 0:
          raise RuntimeError("update_animation was called on a sprite that doesn't have a list of walk down textures.")

      self.cur_texture_index += 1
      if self.cur_texture_index >= len(texture_list):
        self.cur_texture_index = 0

      self.texture = texture_list[self.cur_texture_index]

    if self._texture is None:
      print("Error, no texture set")
    else:
      self.width = self._texture.width * self.scale
      self.height = self._texture.height * self.scale

  def set_texures(self, load_animation_textures:LoadAnimationTextures):
    textures = load_animation_textures.get_texture_group(self._id)
    if textures:
      self.stand_right_textures = textures[1]['right']
      self.stand_left_textures = textures[1]['left']
      self.stand_up_textures = textures[1]['top']
      self.stand_down_textures = textures[1]['bottom']
      self.walk_left_textures = textures[0]['left']
      self.walk_right_textures = textures[0]['right']
      self.walk_up_textures = textures[0]['top']
      self.walk_down_textures = textures[0]['bottom']