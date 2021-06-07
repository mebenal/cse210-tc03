import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):

    def __init__(self):
        super().__init__()
        y = random.randint(2, constants.MAX_Y - 2)
        self.set_position(Point(0, y))
        self.set_velocity(Point(1,0))
        num = random.randint(0, len(constants.LIBRARY))
        self._word = constants.LIBRARY[num]


    def reset_word(self):
        num = random.randint(0, len(constants.LIBRARY))
        self._word = constants.LIBRARY[num]

    def get_word(self):
        return self._word
    
    def set_word(self, word):
        self._word = word
