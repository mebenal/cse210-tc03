from game.actor import Actor
from game.word import Word

class Buffer(Actor):

    def __init__(self):
        self._prompt = "-Buffer: "
        self._player = ""


    def _player_input(self):
        self._prompt
        self._player = input()
        return self._player

    
    def check_word(self):
        if self._word == self._player_input:
            return True 
        


    def get_player_input(self):
        return self._player_input


    def set_player_input(self, string):
        self._player_input = string


    def reset(self):
        return self._player = ""