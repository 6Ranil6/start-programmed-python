from turtle import *
from math import sqrt

showturtle()
setup(600, 600)
pencolor("red")
speed(3)

aggel = 360 / 8
side = 100

for i in range(8):
    right(aggel)  
    forward(side)
nextAggel = (180 - aggel) / 2
right(aggel + (180 - aggel) / 2)
penup()
forward(side / (sqrt(2)/2) )
write("Stop")
