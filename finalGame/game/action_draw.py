from game import constants
from game.action import Action
from game.type_cast import Cast
from game.director_game import DirectorGame
from game.output_service import OutputService

# TODO: Define the DrawActorsAction class here


class ActionDraw(Action):
  def __init__(self, output_service:OutputService):
    self._output_service = output_service

  def execute(self, director:DirectorGame, cast:Cast, frame_count:int):
    self._output_service.draw_layers(cast['map'].get_layers(), constants.DRAW_LAYERS)
    self._output_service.draw_ui(director.get_ui())
