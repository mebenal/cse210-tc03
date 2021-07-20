from arcade.application import View
from game.library_items import LibraryItems
from game.library_sound import LibrarySound
from game.library_animation_textures import LibraryAnimationTextures
from typing import TypedDict


from game.actor_player import Player
from game.map import Map
from game.ui_game import UIGame


class StartMenuCast(TypedDict, total=False):
  map: Map
  player: Player
  views: list[View]
  ui : UIGame
  animation_textures: LibraryAnimationTextures
  sound: LibrarySound
  item_textures: LibraryItems