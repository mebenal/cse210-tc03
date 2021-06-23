import arcade
from game import constants

class Director(arcade.Window):
  def __init__(self):
    super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    self._cast = None
    self._script = None
    self._input_service = None

  def setup(self, cast, script, input_service):
    self._cast = cast
    self._script = script
    self._input_service = input_service       

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

    
  def _cue_action(self, tag):
    for action in self._script[tag]:
      action.execute(self._cast)