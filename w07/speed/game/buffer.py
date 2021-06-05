from game.actor import Actor
from game.word import Word

class Buffer(Actor):


    def _player_input(self, player_input):
        return input(player_input)


    
    def check_word(self, string):
        if self._word == self._player_input:
            return True 
        


    def get_player_input(self):
        return self._player_input


    def set_player_input(self, string):
        self._player_input = string


    def reset(self):
        return self._player_input = "-Buffer: "