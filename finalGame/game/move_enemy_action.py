from game import constants
from game.action import Action


class MoveEnemyAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        cast['enemies'].update()