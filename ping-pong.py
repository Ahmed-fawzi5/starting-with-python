#import turtle module


import turtle

window=turtle.Screen()  #calling class screen from turtle 
window.title("Ping Pong game")  #assigning a name for the window
window.bgcolor("yellow")  #assigning a color for the window 
window.tracer(0) # stopping window from updating
window.setup(width=700,height=400) #setting dimensions of the window


#madrab 1 charactristics
mad1=turtle.Turtle()  #assign madrab 1 
mad1.speed(0)  # fastest speen is zero value
mad1.shape("square")
mad1.color("blue")
mad1.penup() # prevent making lines behind the object 
mad1.goto(-300,0) #assing the position og the object 
mad1.shapesize(stretch_wid=5,stretch_len=1)  #size of the object

#madrab 2 charactristics

mad2=turtle.Turtle()  #assign madrab 2
mad2.speed(0)  # fastest speen is zero value
mad2.shape("square")
mad2.color("red")
mad2.penup() # prevent making lines behind the object 
mad2.goto(300,0) #assing the position og the object 
mad2.shapesize(stretch_wid=5,stretch_len=1)  #size of the object

#the ball

ball=turtle.Turtle()  #ball
ball.speed(0)  # fastest speen is zero value
ball.shape("square")
ball.color("white")
ball.penup() # prevent making lines behind the object 
ball.dx= 0.7
ball.dy= 0.7

# score board 

score1=0
score2=0
score=turtle.Turtle()    #import turtle object
score.penup()            # to not draw any line behinf
score.color("black")
score.goto(0,150)
score.speed(0)
score.hideturtle()       # to hide the object 





#functions for movements :----

#first up
def mad1_up():
    y=mad1.ycor()  #get y cordinate of madrb 1
    y += 20         #  +ve to move up
    mad1.sety(y)   #set y of madrb 1 to the new cordinates of y
# first down
def mad1_down():
    y=mad1.ycor()
    y -= 20           # -ve to move down
    mad1.sety(y)

def mad2_up():
    y=mad2.ycor()
    y += 20
    mad2.sety(y)
# first down
def mad2_down():
    y=mad2.ycor()
    y -= 20
    mad2.sety(y)



#keyboard controls

window.listen()  #prepare window object to accept input
window.onkeypress(mad1_up,"w")   #when I press "W" , the function mad1_up will be called
window.onkeypress(mad1_down,"s")
window.onkeypress(mad2_up,"Up")
window.onkeypress(mad2_down,"Down")


# creating the game loop
while True:
    window.update() #updates the screen each time the game runs 
    score.clear() # tp avoid text overwriting  and show the last score only
    
    #to write text inside the onject and adjust the font and alignment
    score.write("player 1 : {}             player 2 : {} ".format(score1,score2) ,font=("Arial",24,"normal"),align="center")
    


    ball.setx(ball.xcor() + ball.dx)  # ball movement in x direction from 0
    ball.sety(ball.ycor() + ball.dy)  # ball movement in y direction from 0

    # ball bouncing from up , max y = 200px , ball = 20 px
    if ball.ycor() > 190 :  # max broder up
       ball.sety(190)        #bouncing down
       ball.dy *= -1
       
     #ball bouncing from down
    if ball.ycor() < -190 :    
       ball.sety(-190)
       ball.dy *= -1
    #ball brossing right border , max x = 350

    if ball.xcor() > 350 :      #crossing the right border 
       ball.goto(0,0)          # ball goes back to origin
       ball.dx *= -1
       score1 += 1    # adding score to player 1 if the ball passed the right border

     #ball crossing left border
    if ball.xcor() < -350 :
       ball.goto(0,0)
       ball.dx *= -1
       score2 += 1    # adding score to player 2 if the ball passed the right border


       
    if (ball.xcor() < mad2.xcor()) and (ball.xcor() > mad2.xcor() -10) and (ball.ycor() < mad2.ycor()+40 and ball.ycor() > mad2.ycor()-40):  # max broder up0

        ball.setx(mad2.xcor()-10)
        ball.dx *= -1

    if (ball.xcor() < mad1.xcor()) and (ball.xcor() > mad1.xcor() -10) and (ball.ycor() < mad1.ycor()+40 and ball.ycor() > mad1.ycor()-40):  # max broder up0

        ball.setx(mad1.xcor()+10)
        ball.dx *= -1
       

    