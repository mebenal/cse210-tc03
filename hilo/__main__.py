# TODO: Add entry point code here
import random

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        thrower (Thrower): An instance of the class of objects known as Thrower.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 0
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            answer = self.get_inputs()
            self.do_updates(answer)
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
        """
        print(f'The card is: {self.dealer.get_card()}')
        return input("High or Low (H/L)?: ")
        
        
    def do_updates(self, answer):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.points += self.dealer.get_points(answer)
        self.points = self.points * int(self.points > 0)
        self.keep_playing = bool(self.points)

        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f'Next card was: {self.dealer.get_curr_card()}')
        print(f'Your score is: {self.score}')
        if self.keep_playing:
          play_again = input('Keep playing? [y/n] ')
          self.keep_playing = play_again.lower() == 'y'


class Dealer:
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    curr_card = 0
    prev_card = 0

    def __init__(self):
      temp = self.get_card(self)


    def get_card(self):
        self.prev_card = self.curr_card
        self.curr_card = random.randint(1,13)
        return self.curr_card

    def get_points(self, guess):
        if guess.lower() == "h" and self.curr_card > self.prev_card:
            return 100
        elif guess.lower() == "l" and self.curr_card < self.prev_card:
            return -75

