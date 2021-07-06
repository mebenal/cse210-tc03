from game import constants
from game.constants import MapDict
from game.player import Player
from game.enemy import Enemy
from game.item import Item

import os
import arcade
from arcade import tilemap
from arcade import SpriteList
from arcade import Sprite



class Map:
  def __init__(self):
    self._map_list = [tilemap.read_tmx(f'./finalGame/game/maps/{path}') for path in os.listdir('./finalGame/game/maps')]
    self._curr_map = 0
    self._width = 0
    self._height = 0
    self._layers = { 'background' : [ SpriteList(), True  ],
                     'path'       : [ SpriteList(), True  ],
                     'player'     : [ SpriteList(), False ],
                     'enemy'      : [ SpriteList(), False ],
                     'item'       : [ SpriteList(), False ],
                     'collision'  : [ SpriteList(), True  ],
                     'foreground' : [ SpriteList(), True  ],
                     'projectile' : [ SpriteList(), False ]}
    self._set_layers()

  def _set_layers(self):
    self._width = self._map_list[self._curr_map].map_size.width
    self._height = self._map_list[self._curr_map].map_size.height
    for key, value in self._layers.items():
      if key in constants.TILE_LAYERS:
        self._layers[key][0] = tilemap.process_layer( map_object=self._map_list[self._curr_map],
                                                      layer_name=key,
                                                      hit_box_algorithm="Simple",
                                                      scaling=constants.TILE_SCALING,
                                                      use_spatial_hash=value[1] )
    self.replace_layer('player', [Player(self.get_layer('player')[0])])
    self.replace_layer('enemy', [Enemy(enemy) for enemy in self.get_layer('enemy')])
    self.replace_layer('item', [Item(item) for item in self.get_layer('item')])
  
  def load_next_map(self):
    self._curr_map += 1
    self._set_layers()
    

  def get_layers(self) -> MapDict:
    return {k:v[0] for (k,v) in self._layers.items()}

  def get_layer(self, layer) -> SpriteList:
    return self._layers[layer][0]

  def get_map_size(self) -> dict[str:int, str:int]:
    return { "width"  : self._width, 
             "height" : self._height }

  def replace_layer(self, layer:SpriteList, sprite_list:list[Sprite]):
    if len(self._layers[layer][0]) == len(sprite_list):
      for sprite in sprite_list:
        self._layers[layer][0].pop(0)
        self._layers[layer][0].append(sprite)
    else:
       raise Exception("Error: Sprite list must be same length as layer list.")
  

