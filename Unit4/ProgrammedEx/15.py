from turtle import *

showturtle()
setup(600, 600)
pencolor("red")
speed(0)

SideSquare = 10
addSide = 5
for i in range(20):
    for j in range(3):
        left(90)
        forward(SideSquare)
    left(90)
    goto(0,0)
    SideSquare += addSide