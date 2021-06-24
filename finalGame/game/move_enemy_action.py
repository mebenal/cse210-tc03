from finalGame.game import enemy
from game import constants
from game.action import Action
from game.enemy import Enemy
import arcade

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
        for enemy in cast['enemies']:

            if arcade.Sprite.get_distance_between_sprites(cast['player'],enemy) > 10:
                enemy.set_move_behavior(0)
            else:
                enemy.set_move_behavior(1) 
                """
                while self.enemy.fight_or_flight(cast['player'],cast['enemies']) != 0:
                    cast['player']._get_position
                    enemy.change_y = constants.PLAYER_MOVEMENT_SPEED
                    enemy.change_y = -constants.PLAYER_MOVEMENT_SPEED
                    enemy.change_x = -constants.PLAYER_MOVEMENT_SPEED
                    enemy.change_x = constants.PLAYER_MOVEMENT_SPEED
                    """

        cast['enemies'].update()

    


        
        