class Player:

    def __init__(self):
        self.health = 4


    def updateLife(self, check):
        if not check:
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