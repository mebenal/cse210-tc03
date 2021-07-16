from typing import Iterable, TypedDict

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
