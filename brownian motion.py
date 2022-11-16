#import statements
import turtle
from random import randint

class brown:
    
    def __init__(self, n):
        #make empty list of particles
        self.p = []
        
        #setup screen
        self.s = turtle.Screen()
        self.s.setup(500,500)
        self.s.title('Brownian particle motion')
        
        #build desired number of particles
        self.builder(n)
        
        return
    
    def builder(self, n):
        #make n particles and put them in p list
        for i in range(n):
            t = turtle.Turtle()
            t.color('red')
            self.p.append(t)
        return
    
b = brown(5)