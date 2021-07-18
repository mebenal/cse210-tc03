import typing
from arcade.arcade_types import Color


class Text(typing.TypedDict):
  string: str
  start_x: float
  start_y: float
  color: Color
  font_size: int