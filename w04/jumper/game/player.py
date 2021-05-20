class Player:

    def __init__(self):
        self.health = 4


    def updateLife(self, check):
        if not check:
            self.health -= 1
        
    def displayParachute(self): 
        return self.fourhealth()
        

    def fourhealth(self):
        return """  
          ___  
         /___\ 
         \   / 
          \ / 
           0 
          /|\   
          / \ 
                 
        ^^^^^^^"""

    def threehealth(self):
        return """    
         /___\ 
         \   / 
          \ / 
           0 
          /|\   
          / \ 
                 
        ^^^^^^^""" 

    def twohealth(self):
        return """  
         \   / 
          \ / 
           0 
          /|\   
          / \ 
                 
        ^^^^^^^"""

    def onehealth(self):
        return """ 
          \ / 
           0 
          /|\   
          / \ 
                 
        ^^^^^^^"""

    def zerohealth(self):
        return """  
           X
          /|\   
          / \ 
                 
        ^^^^^^^"""