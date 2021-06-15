import random
import math
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self,score):
      self._score = score

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
              bricks.remove(brick)
              ball.set_velocity(ball.get_velocity().reverse_y())
              self._score.add_points(1)
        if math.trunc(ball.get_position().get_x()) in range(paddle.get_position().get_x()-1,paddle.get_position().get_x()+12) and math.trunc(ball.get_position().get_y()) == constants.MAX_Y - 1:
          choice = random.randint(1,2)
          if choice == 1:
            ball.set_velocity(ball.get_velocity().reverse_y())
          elif choice == 2:
            ball.set_velocity(ball.get_velocity().reverse_y())
            ball.set_velocity(ball.get_velocity().reverse_x())