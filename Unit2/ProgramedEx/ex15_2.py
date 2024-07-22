# вторая часть задания 15 

# path a 

# add model turtle and setting phone and pen
import turtle
turtle.showturtle()
turtle.bgcolor("dark blue")
turtle.color("white")
turtle.speed(10)

# add model math for concret data
import math

HYPOTENUES = 175
KATET = HYPOTENUES * math.sqrt(2) / 2
RADIUS = 100 

# Constant point
POINT_1_X = 0
POINT_1_Y = 0

POINT_2_X = -KATET
POINT_2_Y = -KATET

POINT_3_X = KATET
POINT_3_Y = -KATET

POINT_4_X = - 2 * KATET
POINT_4_Y = 0

POINT_5_X = 2 * KATET
POINT_5_Y = 0

# paint five circle

turtle.circle(RADIUS)

turtle.penup()
turtle.goto(POINT_2_X,POINT_2_Y)
turtle.pendown()
turtle.circle(RADIUS)

turtle.penup()
turtle.goto(POINT_3_X,POINT_3_Y)
turtle.pendown()
turtle.circle(RADIUS)

turtle.penup()
turtle.goto(POINT_4_X,POINT_4_Y)
turtle.pendown()
turtle.circle(RADIUS)

turtle.penup()
turtle.goto(POINT_5_X,POINT_5_Y)
turtle.pendown()
turtle.circle(RADIUS)

# delete path a
turtle.reset()

#path b
turtle.color("white")

#CONSTANTS
RAD = 50

DOT_1_X = -200 
DOT_1_Y = 0 + RAD

DOT_2_X = 200
DOT_2_Y = 0 + RAD

DOT_3_X = 0
DOT_3_Y = 200 + RAD

DOT_4_X = 0
DOT_4_Y = -200 + RAD

#DOing circle
turtle.circle(RAD)

#doing line1
turtle.penup()
turtle.goto(DOT_1_X, DOT_1_Y)
turtle.write("Запад")
turtle.pendown()
turtle.goto(DOT_2_X, DOT_2_Y)
turtle.write("Восток")
#doing line2
turtle.penup()
turtle.goto(DOT_3_X, DOT_3_Y)
turtle.write("Север")
turtle.pendown()
turtle.goto(DOT_4_X, DOT_4_Y)
turtle.write("ЮГ")
             
# end setting
turtle.hideturtle()
turtle.done()