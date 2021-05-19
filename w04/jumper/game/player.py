class Player:

    def __init__(self):
        self.health = 4
        self.console = Console()
        self.puzzle = Puzzle()


    def updateLife(self):
        guess = self.console.read("Guess a letter [a-z]: ")
        check = (self.puzzle.checkGuess(guess))
        if check == False:
            self.health -= 1
        
    def displayParachute(self): 
        return self.fourhealth()
        

    def fourhealth():
        return """  
          ___  
         /___\ 
         \   / 
          \ / 
           0 
          /|\   
          / \ 
                 
        ^^^^^^^"""

    def threehealth():
        return """    
         /___\ 
         \   / 
          \ / 
           0 
          /|\   
          / \ 
                 
        ^^^^^^^""" 

    def twohealth():
        return """  
         \   / 
          \ / 
           0 
          /|\   
          / \ 
                 
        ^^^^^^^"""

    def onehealth():
        return """ 
          \ / 
           0 
          /|\   
          / \ 
                 
        ^^^^^^^"""

    def zerohealth():
        return """  
           X
          /|\   
          / \ 
                 
        ^^^^^^^"""