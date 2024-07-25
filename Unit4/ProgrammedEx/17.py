# ex 17

from turtle import *

setup(1000, 1000)
pensize(3)
pencolor("white")
bgcolor("dark blue")
speed(0)
size = 200
agges = 180 - 45

setheading(270)
for counter in range(8):
    forward(size)
    right(agges)
    forward(size)
    
done()
