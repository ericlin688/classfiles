#Import statements
import turtle
from time import sleep
from random import randint, choice
##################

#global variables
score = 0
high_score = 0
delay = 0.2
segments = []
death = False
counter = 0
mat = []
#################

#Screen setup
w = turtle.Screen()
w.bgcolor("light green")
w.setup(600,600)
w.title("Snek")
w.tracer(0)
################

#Snake head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.direction = "none"
################

#Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(20*randint(-14,14),20*randint(-14,14))
##############

#scoreboard
sc = turtle.Turtle()
sc.hideturtle()
sc.penup()
sc.goto(0,260)
sc.write("Score: {}   High Score: {}".format(score,high_score), align = "center", font=("ds-digital",24,"normal"))
##############

#move functions
def up():
    if head.direction != "down":
        head.direction = "up"
    return

def down():
    if head.direction != "up":
        head.direction = "down"
    return

def left():
    if head.direction != "right":
        head.direction = "left"
    return

def right():
    if head.direction != "left":
        head.direction = "right"
    return
################

#keybinds
w.listen()
w.onkeypress(up,"w")
w.onkeypress(down,"s")
w.onkeypress(left,"a")
w.onkeypress(right,"d")
################

#Main loop
while True:
    w.update()
    
    #check border collision
    if head.xcor()>290 or head.ycor()>290 or head.xcor()<-290 or head.ycor()<-290:
        death = True
    #check collision with body
    for s in segments:
        if head.distance(s) == 0:
            death = True
            break
    #######################
        
    #death
    if death:
        head.color("red")
        food.color("purple")
        w.update()
        sleep(0.5)
        score = 0
        sc.clear()
        sc.write("Score: {}   High Score: {}".format(score,high_score), align = "center", font=("ds-digital",24,"normal"))
        for s in segments:
            s.goto(1000,1000)
        segments.clear()
        head.goto(0,0)
        food.goto(20*randint(-14,14),20*randint(-14,14))
        w.update()
        sleep(0.5)
        head.color("black")
        food.color("red")
        head.direction = "none"
        death = False
        delay = 0.2
    ##########
        
    #collision with food
    if head.distance(food) == 0:
        
        #incriment score
        score += 1
        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("Score: {}   High Score: {}".format(score,high_score), align = "center", font=("ds-digital",24,"normal"))
        #################       
  
        #move the food
        food.goto(20*randint(-14,14),20*randint(-14,14))
        w.update()
        #################
        
        #create new body segment
        new = turtle.Turtle()
        new.color("gray")
        new.shape("square")
        new.penup()
        segments.append(new)
        #################
        
        #incriment counter then check for speed increase
        counter += 1
        if counter == 3:
            delay -= delay/10
            counter = 0
    #################
        
    #move body segments (in reverse order)
    for s in range(len(segments)-1,0,-1):
        x = segments[s-1].xcor()
        y = segments[s-1].ycor()
        segments[s].goto(x,y)
    #have lead segment follow head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    ##################
    
    #Move snake head
    if head.direction == "up":
        head.sety(head.ycor()+20)
    
    if head.direction == "down":
        head.sety(head.ycor()-20)
        
    if head.direction == "left":
        head.setx(head.xcor()-20)
    
    if head.direction == "right":
        head.setx(head.xcor()+20)
    ############################
    
    #use game delay
    sleep(delay)
