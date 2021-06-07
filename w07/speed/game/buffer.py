from game.actor import Actor
from game import constants
from game import Point

class Buffer(Actor):

    def __init__(self):
        super().__init__()
        self.set_text("Buffer:")
        self.set_position(Point(0, constants.MAX_Y))
        self._player_input = ""


    
    def check_word(self, string):
        if string == self._player_input:
            return True 
        return False
        


    def get_player_input(self):
        return self._player_input


    def set_player_input(self, string):
        self._player_input = string


    def reset(self):
        self._player_input = ""

    def update_buffer(self):
        self.set_text("Buffer: " + self.set_player_input)