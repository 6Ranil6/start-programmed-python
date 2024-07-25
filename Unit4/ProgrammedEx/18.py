from turtle import *

showturtle()
setup(600, 600)
pencolor("red")
speed(0)

SideSquare = 10
addSide = 5
for i in range(20):
    for j in range(4):
        left(90)
        forward(SideSquare)
        SideSquare += addSide

left(90)
forward(SideSquare)
