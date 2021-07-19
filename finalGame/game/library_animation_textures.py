import math
from typing import List
from arcade import sprite, tilemap
from pytiled_parser.objects import TileSet


class LibraryAnimationTextures:
  def __init__(self, tileset:TileSet):
    if not tileset:
      self._texture_groups_moving = []
      self._texture_groups_static = []
      return
    self._textures: List = []
    for tile in tileset.tiles:
      filename = tilemap._get_image_source(tileset.tiles[tile], None, None)
      image_x, image_y, width, height = tilemap._get_image_info_from_tileset(tileset.tiles[tile])
      self._textures.append(sprite.load_texture(filename, image_x, image_y,
                                        width, height))
    
    texture_row = 0
    texture_group = 0
    self._texture_groups_moving = []
    self._texture_groups_static = []
    for i in range(int(tileset.tile_count/12)):
      self._texture_groups_moving.append([{'left':[],'right':[],'top':[],'bottom':[]},[]])
      self._texture_groups_static.append([{'left':[],'right':[],'top':[],'bottom':[]},[]])
    
    groups = ['bottom', 'left', 'right', 'top']

    for i, texture in enumerate(self._textures):
      if i % 3 == 0:
        texture_group += 1
      if i % tileset.columns == 0:
        row = math.trunc(i / tileset.columns)
        texture_group = 0
        if row % 4 == 0 and row != 0:
          texture_row += 1
      texture_group_index = int(texture_row * (tileset.columns / 3) + texture_group)
      self._texture_groups_moving[texture_group_index][0][groups[row % 4]].append(texture)
      self._texture_groups_moving[texture_group_index][1].append(i)
    for i, group in enumerate(self._texture_groups_static):
      for direction in groups:
        group[0][direction].append(self._texture_groups_moving[i][0][direction][1])
      group[1] = self._texture_groups_moving[i][1]
  
  def get_texture_group(self, id:int) -> list[list, list]:
    for i, group in enumerate(self._texture_groups_moving):
      if id in group[1]:
        return [group[0], self._texture_groups_static[i][0]]
    return None
