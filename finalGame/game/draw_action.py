from game import constants
from game.action import Action

# TODO: Define the DrawActorsAction class here


class DrawAction(Action):
  def __init__(self, output_service):
    self._output_service = output_service

  def execute(self, cast, frame_count):
    self._output_service.draw_layers(cast['map'].get_layers(), constants.LAYERS)