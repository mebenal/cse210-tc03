SCREEN_WIDTH = 1420
SCREEN_HEIGHT = 700
SCREEN_TITLE = 'Hero Man v0.0.1'
#1080
#1920
CHARACTER_SCALING = 3
ITEM_SCALING = 2
TILE_SCALING = 8
SPRITE_PIXEL_SIZE = 16
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

PLAYER_MOVEMENT_SPEED = 5
ENEMY_MOVEMENT_SPEED = 2
PROJECTILE_SPEED = 20

ENEMY_SIGHT = 250

TILE_LAYERS = ['background', 'path', 'collision', 'player', 'enemy', 'item', 'foreground']
DRAW_LAYERS = ['background', 'path', 'collision', 'player', 'enemy', 'item', 'projectile', 'foreground']


from typing import Iterable, TypedDict

class Mouse(TypedDict):
  x_pos: int
  y_pos: int

from arcade import SpriteList

class MapDict(TypedDict):
  background: SpriteList
  path:       SpriteList
  player:     SpriteList
  enemy:      SpriteList
  item:       SpriteList
  collision:  SpriteList
  foreground: SpriteList
  projectile: SpriteList


from game.ui import UI
from game.map import Map
from game.item import Item
from game.enemy import Enemy
from game.player import Player
from game.projectile import Projectile

from arcade import PhysicsEngineSimple

class Cast(TypedDict, total=False):
  map: Map
  player: Player
  enemies: Iterable[Enemy]
  items: Iterable[Item]
  physics_engines: list[PhysicsEngineSimple]
  mouse: Mouse
  projectiles: Iterable[Projectile]
  ui : UI