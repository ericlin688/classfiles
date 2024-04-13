import turtle
import deckocards
from time import sleep

#to do list
#get card special rules to work
#cleanup function and reshuffle function
#create gamestates/state machine
#change direction swapped with custom card
    #custom card is give random card to opponent from hand

w = turtle.Screen()
w.tracer(0)
w.register_shape("unocard.gif")

#pen init
pen = turtle.Turtle()
pen.color('orange')
pen.hideturtle()
pen.pensize(5)
################

#pen functions
def move(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    return
#################

#pen draw at start
pen.penup()
pen.goto(-200,0)
pen.forward(-55)
pen.pendown()
pen.left(90)
pen.forward(80)
pen.right(90)
pen.forward(110)
pen.right(90)
pen.forward(160)
pen.right(90)
pen.forward(110)
pen.right(90)
pen.forward(80)
pen.right(90)

pen.color("blue")
pen.penup()
pen.goto(200,0)
pen.forward(-55)
pen.pendown()
pen.left(90)
pen.forward(80)
pen.right(90)
pen.forward(110)
pen.right(90)
pen.forward(160)
pen.right(90)
pen.forward(110)
pen.right(90)
pen.forward(80)

pen.penup()
pen.goto(-200,0)
pen.shape("unocard.gif")
pen.showturtle()
w.update()
#######################

#user control functions
def clicky(x,y):
    w.onclick(None)
    #draw a card
    if x > -255 and x < -145 and y < 80 and y > -80:
        d.draw(1)
        c = card(d.hand[-1][0],d.hand[-1][1])
        cards.append(c)
        
        for i in range(len(d.hand)):
            cards[i].card.clear()
            cards[i].paintcard(-320+735*i/len(d.hand),-200)
        aiturn()
        w.onclick(clicky)
        return
    #play a card        
    for i in range(len(cards)-1,-1,-1):
        if abs(cards[i].card.xcor()-x) < 50 and abs(cards[i].card.ycor()-y) < 75 and (cards[i].value == discard[-1].value or cards[i].color == discard[-1].color or cards[i].color == 'purple' or discard[-1].color == 'purple'):
            cards[i].card.clear()
            d.discard.append(d.hand.pop(i))
            discard.append(cards.pop(i))
            if len(discard) == 1:
                discard[0].paintcard(200,0)
            elif len(discard) > 1:
                discard[-2].card.clear()
                discard[-1].paintcard(200,0)
            aiturn()
            break
    w.onclick(clicky)
    return   
#######################

#ai control
def aiturn():
    if len(cards)==0:
        w.clear()
        move(0,0)
        pen.color("black")
        pen.write("YOU WIN!",False,"center",("Trebuchet MS",100,"bold"))
        sleep(3)
        quit()
        #player wins
    sleep(1)
    play = False
    for i in range(len(aicards)):
        if aicards[i].value == discard[-1].value or aicards[i].color == discard[-1].color or aicards[i].color == "purple" or discard[-1].color == "purple":
            aicards[i].card.shape("arrow")
            aicards[i].card.hideturtle()
            d.discard.append(d.aihand.pop(i))
            discard.append(aicards.pop(i))
            discard[-2].card.clear()
            discard[-1].paintcard(200,0)
            play = True
            break
    if not play:
        d.aidraw(1)
        aicards.append(card(d.aihand[-1][0],d.aihand[-1][1]))
        aicards[-1].card.shape("unocard.gif")
        aicards[-1].card.showturtle()
        aicards[-1].card.penup()
    for i in range(len(aicards)):
        aicards[i].card.goto(-320+735*i/len(d.aihand),200)
    w.update()
    if len(aicards)==0:
        w.clear()
        move(0,0)
        pen.color("black")
        pen.write("YOU LOSE!",False,"center",("Trebuchet MS",100,"bold"))
        sleep(3)
        quit()
        #player loses
    return
#######################

#visual card
class card:

    def __init__(self,value = '',color = 'black'):
        self.card = turtle.Turtle()
        self.card.hideturtle()
        self.card.fillcolor(color)
        self.color = color
        self.value = value
        return

    def move(self,x,y):
        self.card.penup()
        self.card.goto(x,y)
        self.card.pendown()
        return

    def paintcard(self,x,y):
        self.move(x,y)
        self.move(self.card.xcor()-50,self.card.ycor())
        self.card.left(90)
        self.card.begin_fill()
        self.card.forward(75)
        self.card.right(90)
        self.card.forward(100)
        self.card.right(90)
        self.card.forward(150)
        self.card.right(90)
        self.card.forward(100)
        self.card.right(90)
        self.card.forward(75)
        self.card.end_fill()
        self.card.right(90)
        self.move(self.card.xcor()+50,self.card.ycor())
        self.card.write(self.value,False,'center',('Arial',34,'bold'))
        self.move(self.card.xcor()-37,self.card.ycor()+53)
        self.card.write(self.value,False,'center',('Arial',12,'normal'))
        self.move(self.card.xcor()+37,self.card.ycor()-53)
        w.update()
        return
###########################
    
#card dealing functions
def burn(n):
    for i in range(n):
        d.burn(1)
        discard.append(card(d.discard[0][0],d.discard[0][1]))
        discard[0].paintcard(200,0)
    return

def player_draw(n):
    for i in range(n):
        d.draw(1)
        cards.append(card(d.hand[-1][0],d.hand[-1][1]))

    for i in range(len(d.hand)):
        cards[i].card.clear() #don't need at beginning. will need if make state machine.
        cards[i].paintcard(-320+735*i/len(d.hand),-200)
    return

def ai_draw(n):
    for i in range(n):
        d.aidraw(1)
        aicards.append(card(d.aihand[-1][0],d.aihand[-1][1]))

    for i in range(len(d.aihand)):
        aicards[i].card.shape("unocard.gif")
        aicards[i].card.showturtle()
        aicards[i].card.penup()
        aicards[i].card.goto(-320+735*i/len(d.aihand),200)
    return
###########################
    
#card drawing init
d = deckocards.Deck()
d.shuffledeck()

cards = []
aicards = []
discard = []
###########################

    #discard 1 card at start
burn(1)

    #player draw 7 at start
player_draw(7)

    #ai draw 7 at start
ai_draw(7)

w.update()
#######################

w.onclick(clicky)
w.listen()

w.mainloop()