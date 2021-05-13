import random

class Dealer:
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    curr_card = 0
    prev_card = 0

    def get_card(self):
        self.prev_card = random.randint(1,13)

    def get_points(self, guess):
        self.curr_card = self.get_card()
        if guess.lower() == "h" and self.curr_card > self.prev_card:
            return 100
        elif guess.lower() == "l" and self.curr_card < self.prev_card:
            return -75

        