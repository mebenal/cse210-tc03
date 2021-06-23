import random
import math
import arcade
import os
from game import constants
from game.test import Test
from game.director import Director
from game.player import Player
from game.enemy import Enemy
from game.point import Point
from game.score import Score
from game.map import Map
from game.move_player_action import MovePlayerAction
from game.move_enemy_action import MoveEnemyAction
from game.draw_action import DrawAction
from game.handle_collisions_action import HandleCollisionsAction
from game.input_service import InputService
from game.output_service import OutputService

def main():
    # create the cast {key: tag, value: list}
    cast = {}
    cast['map'] = Map()
    cast['player'] = Player(cast['map'].get_layers()['player'][0])
    cast['enemies'] = [Enemy(enemy) for enemy in cast['map'].get_layers()['enemy']]
    cast['map'].replace_layer('player', [cast['player']])
    cast['map'].replace_layer('enemy', cast['enemies'])
    cast['enemies'] = cast['map'].get_layers()['enemy']
    cast['physics_engines'] = [arcade.PhysicsEngineSimple(cast['player'], cast['map'].get_layers()['collision'])]
    input_service = InputService()

    script = {}
    script['input'] = [MovePlayerAction(input_service)]
    script['update'] = [HandleCollisionsAction(), MoveEnemyAction()]
    script['output'] = [DrawAction(OutputService())]
    test = Test()
    test.setup(cast, script, input_service)
    arcade.run()
    return
    
    # create the script {key: tag, value: list}
    handle_collisions_acition = HandleCollisionsAction(score)
    
    script["update"] = [move_actors_action, handle_collisions_acition]

    # start the game
    director = Director(cast, script, input_service)
    director.setup()
    director.run()

if __name__ == "__main__":
    main()