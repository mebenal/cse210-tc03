import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

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
        if ball.get_position().get_x() in range(paddle.get_position().get_x(),paddle.get_position().get_x()+8) and ball.get_position().get_y() == constants.MAX_Y - 2:
          ball.set_velocity(ball.get_velocity().reverse_y())