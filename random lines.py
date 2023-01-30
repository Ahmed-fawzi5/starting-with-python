from turtle import *
import turtle as tur
import random
import math

tur.setup(900,500)
tur.title("Python Guides")
a1 = tur.Turtle()
b1 = tur.Turtle()
c1 = tur.Turtle()
d1 = tur.Turtle()
e1 = tur.Turtle()

a1.color('cyan')
b1.color('red')
c1.color('purple')
d1.color('yellow')
e1.color('red')

turtlist = []
turtlist.append(a1)
turtlist.append(b1)
turtlist.append(c1)
turtlist.append(d1)
turtlist.append(e1)

tur.speed(0)
tur.tracer(0)
tur.hideturtle()
sum = 0
count = 0
for j in range(100):
    for i in range(10000):
        for turt in turtlist:
            turt.seth(random.randrange(0,360,90))
            turt.fd(10)
        tur.update()
    for turt in turtlist:
        sum += math.sqrt(turt.xcor()*turt.xcor() + turt.ycor()*turt.ycor())/10*2*math.sqrt(turt.xcor()*turt.xcor() + turt.ycor()*turt.ycor())/10*2/100
        count += 1
    for turt in turtlist:
        turt.clear()
        turt.up()
        turt.goto(0,0)
        turt.down()
    print(sum/count)
