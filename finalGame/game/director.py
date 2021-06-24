import arcade
from game import constants
import timeit

class Director(arcade.Window):
  def __init__(self):
    super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    self._cast = None
    self._script = None
    self._input_service = None

    '''
    self.processing_time = 0
    # Time for on_draw
    self.draw_time = 0
    # Variables used to calculate frames per second
    self.frame_count = 0
    self.fps_start_timer = None
    self.fps = None
    '''

  def setup(self, cast, script, input_service):
    self._cast = cast
    self._script = script
    self._input_service = input_service       

  def on_draw(self):
    '''
    # Start timing how long this takes
    start_time = timeit.default_timer()
    # --- Calculate FPS
    fps_calculation_freq = 60
    # Once every 60 frames, calculate our FPS
    if self.frame_count % fps_calculation_freq == 0:
      # Do we have a start time?
      if self.fps_start_timer is not None:
        # Calculate FPS
        total_time = timeit.default_timer() - self.fps_start_timer
        self.fps = fps_calculation_freq / total_time
      # Reset the timer
      self.fps_start_timer = timeit.default_timer()
    # Add one to our frame count
    self.frame_count += 1
    '''

    arcade.start_render()
    self._cue_action('output')

    '''
    height = arcade.get_viewport()[3]
    width = arcade.get_viewport()[0]
    # Display timings
    output = f"Processing time: {self.processing_time:.5f}"
    arcade.draw_text(output, width, height - 25, arcade.color.BLACK, 18)
    output = f"Drawing time: {self.draw_time:.5f}"
    arcade.draw_text(output, width, height - 50, arcade.color.BLACK, 18)
    if self.fps is not None:
      output = f"FPS: {self.fps:.0f}"
      arcade.draw_text(output, width, height - 75, arcade.color.BLACK, 18)
    # Stop the draw timer, and calculate total on_draw time.
    self.draw_time = timeit.default_timer() - start_time
    '''

  def on_key_press(self, symbol, modifiers):
    self._input_service.set_key(symbol, modifiers)
    self._cue_action('input')

  def on_key_release(self, symbol, modifiers):
    self._input_service.remove_key(symbol, modifiers)
    self._cue_action('input')

  def on_update(self, delta_time):
    
    # Start timing how long this takes
    start_time = timeit.default_timer()
    

    self._cue_action('update')

    
    # Stop the draw timer, and calculate total on_draw time.
    self.processing_time = timeit.default_timer() - start_time
    

  def _cue_action(self, tag):
    for action in self._script[tag]:
      action.execute(self._cast)