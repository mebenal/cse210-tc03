from game import constants
from game.action import Action
from game.type_game_cast import GameCast
from game.director_game import DirectorGame
from game.output_service import OutputService

# TODO: Define the DrawActorsAction class here


class ActionDraw(Action):
  def __init__(self, output_service:OutputService):
    self._output_service = output_service

  def execute(self, director:DirectorGame, cast:GameCast, frame_count:int):
    self._output_service.draw_layers(cast['map'].get_layers(), constants.DRAW_LAYERS)
    self._output_service.draw_ui(cast['ui'])
