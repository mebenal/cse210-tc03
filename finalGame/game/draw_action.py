from game import constants
from game.action import Action
from game.constants import Cast
from game.director import Director
from game.output_service import OutputService

# TODO: Define the DrawActorsAction class here


class DrawAction(Action):
  def __init__(self, output_service:OutputService):
    self._output_service = output_service

  def execute(self, director:Director, cast:Cast, frame_count:int):
    self._output_service.draw_layers(cast['map'].get_layers(), constants.DRAW_LAYERS)
