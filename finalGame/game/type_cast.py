from game.ui_start_menu import UIStartMenu
from arcade.application import View
from game.library_items import LibraryItems
from game.library_sound import LibrarySound
from game.library_animation_textures import LibraryAnimationTextures
from typing import Iterable, TypedDict

from arcade import PhysicsEngineSimple
from arcade.texture import Texture

from game.actor_enemy import Enemy
from game.actor_player import Player
from game.item import Item
from game.map import Map
from game.projectile import Projectile
from game.type_mouse import Mouse
from game.ui_game import UIGame


class Cast(TypedDict, total=False):
  map: Map
  player: Player
  enemies: Iterable[Enemy]
  items: Iterable[Item]
  physics_engines: list[PhysicsEngineSimple]
  mouse: Mouse
  projectiles: Iterable[Projectile]
  ui : list[UIGame,UIStartMenu]
  animation_textures: LibraryAnimationTextures
  sound: LibrarySound
  item_textures: LibraryItems
  views: list[View]
