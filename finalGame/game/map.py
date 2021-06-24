import arcade
from game import constants
import os

class Map:
  def __init__(self):
    self._map_list = [arcade.tilemap.read_tmx(f'./finalGame/game/maps/{path}') for path in os.listdir('./finalGame/game/maps')]
    self._curr_map = 0
    self._width = 0
    self._height = 0
    self._layers = { 'background' : [ arcade.SpriteList(), True  ],
                     'path'       : [ arcade.SpriteList(), True  ],
                     'player'     : [ arcade.SpriteList(), False ],
                     'enemy'      : [ arcade.SpriteList(), False ],
                     'item'       : [ arcade.SpriteList(), True  ],
                     'collision'  : [ arcade.SpriteList(), True  ],
                     'foreground' : [ arcade.SpriteList(), True  ] }
    self._set_layers()

  def _set_layers(self):
    self._width = self._map_list[self._curr_map].map_size.width
    self._height = self._map_list[self._curr_map].map_size.height
    for key, value in self._layers.items():
      self._layers[key][0] = arcade.tilemap.process_layer( map_object=self._map_list[self._curr_map],
                                                           layer_name=key,
                                                           hit_box_algorithm="Simple",
                                                           scaling=constants.TILE_SCALING,
                                                           use_spatial_hash=value[1] )

  def load_next_map(self):
    self._curr_map += 1
    self._set_layers()

  def get_layers(self):
    return {k:v[0] for (k,v) in self._layers.items()}

  def get_layer(self, layer):
    return self._layers[layer][0]

  def get_map_size(self):
    return { "width"  : self._width, 
             "height" : self._height }

  def replace_layer(self, layer, sprite_list):
    if len(self._layers[layer][0]) == len(sprite_list):
      for sprite in sprite_list:
        self._layers[layer][0].pop(0)
        self._layers[layer][0].append(sprite)
    else:
       raise Exception("Error: Sprite list must be same length as layer list.")
