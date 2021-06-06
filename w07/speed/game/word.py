import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):

    def __init__(self):
        select = []
        with open("words.txt") as words:
            for i in range(len(words)):
                select.append(words[i])
        num = random.randint(0, len(words))
        self.word = select[num]

    def reset_word(self):
        None