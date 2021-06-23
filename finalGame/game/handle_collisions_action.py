from game import constants
from game.action import Action
import arcade

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
      self.view_left = 0
      self.view_bottom = 0

    def execute(self, cast):
      """Executes the action using the given actors.

      Args:
          cast (dict): The game actors {key: tag, value: list}.
      """
      for engine in cast['physics_engines']:
        engine.update()

      cast['map'].get_layers()['collision'].update_animation()
      cast['map'].get_layers()['background'].update_animation()
      changed = False

      # Scroll left
      left_boundary = self.view_left + constants.LEFT_VIEWPORT_MARGIN
      if cast['player'].left < left_boundary:
        self.view_left -= left_boundary - cast['player'].left
        changed = True

      # Scroll right
      right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_VIEWPORT_MARGIN
      if cast['player'].right > right_boundary:
        self.view_left += cast['player'].right - right_boundary
        changed = True

      # Scroll up
      top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.TOP_VIEWPORT_MARGIN
      if cast['player'].top > top_boundary:
        self.view_bottom += cast['player'].top - top_boundary
        changed = True

      # Scroll down
      bottom_boundary = self.view_bottom + constants.BOTTOM_VIEWPORT_MARGIN
      if cast['player'].bottom < bottom_boundary:
        self.view_bottom -= bottom_boundary - cast['player'].bottom
        changed = True

      if changed:
        # Only scroll to integers. Otherwise we end up with pixels that
        # don't line up on the screen
        self.view_bottom = int(self.view_bottom)
        self.view_left = int(self.view_left)

        # Do the scrolling
        arcade.set_viewport(self.view_left,
                            constants.SCREEN_WIDTH + self.view_left,
                            self.view_bottom,
                            constants.SCREEN_HEIGHT + self.view_bottom)