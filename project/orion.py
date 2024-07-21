# создаем карту созвездия орион при помощи модуля turtle
import turtle 
turtle.showturtle() # отображаем черепашку на карте
turtle.speed(0) # чтобы мгновенно выводилось всё

# наводим красоту
turtle.bgcolor("dark blue")
turtle.color("white")

# вводим поименнованые константы 
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# зададим размер графического окна
turtle.setup(500, 600)

# Наносим точки звезд и сразу пишем их название
turtle.penup()

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.dot()
turtle.write("Бетельгейзе")

turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.dot()
turtle.write("Хатиса")


turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.dot()
turtle.write("Альнитак")

turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.dot()
turtle.write("Альнилам")

turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.dot()
turtle.write("Минтака")

turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.dot()
turtle.write("Саиф")


turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.dot()
turtle.write("Ригель")

#черчим линии
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown() # отпускаем перо
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.penup()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.penup()

# оставляем окно открытым
turtle.hideturtle()
turtle.done()
