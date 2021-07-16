from typing import Iterable, TypedDict

from arcade import PhysicsEngineSimple, SpriteList

from game.actor_enemy import Enemy
from game.actor_player import Player
from game.item import Item
from game.map import Map
from game.projectile import Projectile
from game.type_mouse import Mouse
from game.ui import UI


class GameCast(TypedDict, total=False):
  map: Map
  player: Player
  enemies: Iterable[Enemy]
  items: Iterable[Item]
  physics_engines: list[PhysicsEngineSimple]
  mouse: Mouse
  projectiles: Iterable[Projectile]
  ui : UI
