import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):

    def __init__(self, y):
        super().__init__()
        x = random.randint(1, constants.MAX_X - 1)
        self.set_position(Point(x, y))
        self.set_velocity(Point(1+(y%2*-2),0))
        self.reset_word()


    def reset_word(self):
        num = random.randint(0, len(constants.LIBRARY))
        self._word = constants.LIBRARY[num]
        if self.get_velocity().get_x() == 1:
          self.set_text(f">>-{self._word}-->")
        else:
          self.set_text(f"<--{self._word}-<<")


    def get_word(self):
        return self._word
    
    def set_word(self, word):
        self._word = word
    
    def move_next(self):
        x1 = self._position.get_x()
        y1 = self._position.get_y()
        x2 = self._velocity.get_x()
        y2 = self._velocity.get_y()
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1 - abs(len(self._word)))
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        self._position = position
