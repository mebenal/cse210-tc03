import random
import math
import arcade
import os
from game import constants
from game.director import Director
from game.player import Player
from game.enemy import Enemy
from game.point import Point
from game.score import Score
from game.map import Map
from game.move_player_action import MovePlayerAction
from game.move_enemy_action import MoveEnemyAction
from game.handle_viewport_action import HandleViewportAction
from game.handle_collisions_action import HandleCollisionsAction
from game.draw_action import DrawAction
from game.input_service import InputService
from game.output_service import OutputService

def main():
    # create the cast {key: tag, value: list}
    cast = {}
    cast['map'] = Map()
    cast['player'] = Player(cast['map'].get_layer('player')[0])
    cast['enemies'] = [Enemy(enemy) for enemy in cast['map'].get_layer('enemy')]
    cast['map'].replace_layer('player', [cast['player']])
    cast['map'].replace_layer('enemy', cast['enemies'])
    cast['enemies'] = cast['map'].get_layer('enemy')
    cast['physics_engines'] = [arcade.PhysicsEngineSimple(cast['player'], cast['map'].get_layer('collision'))]
    input_service = InputService()

    script = {}
    script['input'] = [MovePlayerAction(input_service)]
    script['update'] = [HandleCollisionsAction(), MoveEnemyAction(), HandleViewportAction()]
    script['output'] = [DrawAction(OutputService())]
    director = Director()
    director.setup(cast, script, input_service)
    arcade.run()

if __name__ == "__main__":
    main()