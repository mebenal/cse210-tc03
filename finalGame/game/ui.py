import random


class UI:
  """Points earned. The responsibility of Score is to keep track of the player's points.

  Stereotype:
    Information Holder

  Attributes: 
    _points (integer): The number of points the food is worth.
  """
  
  def __init__(self):
    """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
    Args:
      self (Score): an instance of Score.
    """
       
    
    