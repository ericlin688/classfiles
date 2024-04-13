from random import shuffle

class Deck:
    
    def __init__(self):
        self.deck = []
        self.hand = []
        self.aihand = []
        self.discard = []
        for i in range(10):
            for color in ['Red','Yellow','Green','Blue']:
                for face in ['1','2','3','4','5','6','7','8','9','10','(x)','+2','<--']:
                    self.deck.append([face,color])
            self.deck.append(['+4','purple'])
            self.deck.append(['+4','purple'])
            self.deck.append(['rgby','purple'])
            self.deck.append(['rgby','purple'])
        return
    
    def showdeck(self):
        for card in self.deck:
            print(card)
        return
    
    def shuffledeck(self):
        shuffle(self.deck)
        return
    
    def draw(self,n):
        for i in range(n):
            self.hand.append(self.deck.pop())
        return
    
    def aidraw(self,n):
        for i in range(n):
            self.aihand.append(self.deck.pop())
    
    def showhand(self):
        return self.hand
    
    def burn(self,n):
        for i in range(n):
            self.discard.append(self.deck.pop())
        return
