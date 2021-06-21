import arcade
from game import constants
import os

class Map:
  def __init__(self):
    self.map_list = [arcade.tilemap.read_tmx(f'./finalGame/game/maps/{path}') for path in os.listdir('./finalGame/game/maps')]
    self.curr_map = 0
    self.layers = { 'background' : arcade.SpriteList(),
                    'path' :       arcade.SpriteList(),
                    'collision' :  arcade.SpriteList(),
                    'foreground' : arcade.SpriteList() }
    self._set_layers()
    
                                  
  def _set_layers(self):
    for key, value in self.layers.items():
      self.layers[key] = arcade.tilemap.process_layer(map_object=self.map_list[self.curr_map],
                                           layer_name=key,
                                           scaling=constants.TILE_SCALING,
                                           use_spatial_hash=True)

  def load_next_map(self):
    self.curr_map += 1
    self._set_layers()

  def get_layers(self):
    return self.layers