from arcade.sprite_list import SpriteList
from game import constants
from game.director import Director
from game.map import Map
from game.constants import Cast
from game.player_action import PlayerAction
from game.move_enemy_action import MoveEnemyAction
from game.handle_viewport_action import HandleViewportAction
from game.handle_items_action import HandleItemsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_attack_action import HandleAttackAction
from game.update_cast import UpdateCast
from game.draw_action import DrawAction
from game.input_service import InputService
from game.output_service import OutputService

import arcade
from arcade import PhysicsEngineSimple
from typing import Iterable, List, TypedDict

def main():
  # create the cast {key: tag, value: list}
  cast: Cast = {}
  cast['map'] = Map()
  cast['player'] = cast['map'].get_layer('player')[0]
  cast['enemies'] = cast['map'].get_layer('enemy')
  cast['items'] = cast['map'].get_layer('item')
  cast['projectiles'] = cast['map'].get_layer('projectile')
  cast['physics_engines'] = [PhysicsEngineSimple(cast['player'], cast['map'].get_layer('collision'))]
  cast['mouse'] = {'x_pos' : 0, 'y_pos' : 0}

  input_service = InputService()
  
  script = {}
  script['input'] = [PlayerAction(input_service)]
  script['update'] = [HandleCollisionsAction(), MoveEnemyAction(), HandleViewportAction(), HandleItemsAction(), HandleAttackAction(), UpdateCast()]
  script['output'] = [DrawAction(OutputService())]
  director = Director()
  director.setup(cast, script, input_service)
  arcade.run()

if __name__ == "__main__":
  main()