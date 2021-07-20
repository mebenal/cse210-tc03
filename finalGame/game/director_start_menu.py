from game.ui_start_menu import UIStartMenu
from game.type_cast import Cast
from game.input_service import InputService

import arcade

class DirectorStartMenu(arcade.View):
  def __init__(self,window):
    self.window = window
    self._cast = None
    self._script = None
    self._input_service = None

  def setup(self, cast:Cast, script:list, input_service:InputService):
    self._cast:Cast = cast
    self._script:list = script
    self._input_service:InputService = input_service
    

  def on_draw(self):

    arcade.start_render()
    self._cue_action('output')


  def on_key_press(self, symbol, modifiers):
    self._input_service.set_key(symbol, modifiers)
    self._cue_action('input')

  def on_key_release(self, symbol, modifiers):
    self._input_service.remove_key(symbol, modifiers)
    self._cue_action('input')

  def on_update(self, delta_time):

    self._cue_action('update')


  def _cue_action(self, tag:str):
    for action in self._script[tag]:
      action.execute(self, self._cast, 0)
  
  def get_ui(self) -> UIStartMenu:
    return self._cast['ui'][0]