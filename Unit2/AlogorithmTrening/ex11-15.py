#ex11
number = 1234567.456
print(f"{number:,.1f}")
#ex12
#Ответ: Джордж@Джон@Пол@Ринго
#ex13
import turtle
turtle.showturtle()
turtle.circle(75)
#ex14
# import turtle
turtle.showturtle()
turtle.begin_fill()
for a in range(3):
    turtle.forward(100)
    turtle.left(90)
turtle.forward(100)
turtle.end_fill()
# ex 15
import turtle
turtle.begin_fill()
turtle.fillcolor("red")
turtle.penup()
turtle.setheading(270)
turtle.goto(-30, 50)
turtle.pendown()
turtle.circle(80)
turtle.end_fill()

turtle.begin_fill()
turtle.fillcolor("white")
turtle.penup()
turtle.goto(0, 0)
turtle.setheading(0)
turtle.pendown()
for a in range(3):
    turtle.forward(100)
    turtle.left(90)
turtle.forward(100)
turtle.end_fill()