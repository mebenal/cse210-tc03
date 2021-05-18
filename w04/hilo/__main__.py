# TODO: Add entry point code here
import random


class Director:
  """A code template for a person who directs the game. The responsibility of 
  this class of objects is to keep track of the points and control the 
  sequence of play.
  Attributes:
      keep_playing (boolean): Whether or not the player wants to keep playing
                              if they haven't lost.
      points (int): The total number of points earned.
      dealer (Dealer): An instance of the class of objects known as Dealer.
  """
  
  def __init__(self):
    """The class constructor.
    Args:
        self (Director): an instance of Director.
    """
    self.keep_playing = True
    self.points = 0
    self.dealer = Dealer()
  
  def start_game(self):
    """Starts the game loop to control the sequence of play.
    Args:
        self (Director): an instance of Director.
    """
    self.points = 300
    while self.keep_playing:
      answer = self.get_inputs()
      self.do_updates(answer)
      self.do_outputs()
  
  def get_inputs(self):
    """Gets the inputs at the beginning of each round of play. In this case,
    that means showing the current card and asking the user for hi or low.
    Args:
        self (Director): An instance of Director.
    """
    print(f'The card is: {self.dealer.get_curr_card()}')
    return input("High or Low (H/L)?: ")
  
  def do_updates(self, answer):
    """Updates the important game information for each round of play. In 
    this case, that means updating the points and determining whether they
    lost the game.
    Args:
        self (Director): An instance of Director.
        answer (str): Whether the user choose hi or low.
    """
    self.dealer.get_card()
    self.points += self.dealer.get_points(answer)
    self.points = self.points * int(self.points > 0)
    self.keep_playing = bool(self.points)
  
  def do_outputs(self):
    """Outputs the important game information for each round of play. In 
    this case, that means what the next card was, what their score is, and
    whether they want to keep playing if they haven't lost the game.
    Args:
        self (Director): An instance of Director.
    """
    print(f'Next card was: {self.dealer.get_curr_card()}')
    print(f'Your score is: {self.points}')
    if self.keep_playing:
      play_again = input('Keep playing? [y/n] ')
      self.keep_playing = play_again.lower() == 'y'
      print('')


class Dealer:
  cards = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
  curr_card = 0
  prev_card = 0

  def __init__(self):
    self.get_card()

  def get_card(self):
    self.prev_card = self.curr_card
    self.curr_card = random.randint(0, len(self.cards) - 1)
    return self.curr_card

  def get_points(self, guess):
    is_valid = guess.lower() == "h" and self.curr_card > self.prev_card or \
      guess.lower() == "l" and self.curr_card < self.prev_card
    return int(is_valid) * 100 + int(not is_valid) * -75

  def get_curr_card(self):
    return self.cards[self.curr_card]


director = Director()
director.start_game()
