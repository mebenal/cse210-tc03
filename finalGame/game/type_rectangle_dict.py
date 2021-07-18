from typing import TypedDict
from arcade import Shape

class RectangleDict(TypedDict):
  player_weapon_cooldown: Shape
  player_health_outline : Shape
  player_health_bar: Shape
  